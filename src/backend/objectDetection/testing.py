import os
import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import numpy as np
import crop_images as ci
from PIL import Image
import Bird as b
import nameToParsedWikiArticle as ntp 

#Google cloud vision API detection
def get_bird_box(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    path = os.path.join(os.path.dirname(__file__), path)
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    output = []
    for object_ in objects:
        if object_.name == "Bird":
            x = []
            y = []
            for vertex in object_.bounding_poly.normalized_vertices:
                x.append(vertex.x)
                y.append(vertex.y)
            output.append((min(x), min(y), max(x), max(y)))
    return output
def make_img_array(filename):
    raw = tf.io.read_file(filename)
    image = tf.image.decode_png(raw, channels=3)
    #make pixel values between 0 and 1
    
    return image

def what_bird(img):
    '''Returns the index of the bird in the list of birds'''

    m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1')
    clasifier = tf.keras.Sequential([m])
    
    out = clasifier.predict(img[np.newaxis, ...])
    # print(out)
    return int(tf.math.argmax(out[0], axis=-1).numpy())



def make_birds(path):

    img = Image.open(os.path.dirname(__file__), path)   
    print(get_bird_box(path))
    bounding_boxes = get_bird_box(path)
    cropped = ci.crop_and_process(img, bounding_boxes)
    birds = []
    for img in range(cropped):
        scientific_name = what_bird(cropped[img])
        birds.append(b.Bird(name= ntp.getNameFromScientificName(scientific_name),
                            scientific_name=scientific_name, 
                            description=ntp.getSummary(scientific_name),
                            bounding_box=bounding_boxes[img]))
    return birds

def main():
    img = Image.open(r'src/backend/objectDetection/images/ducks.jpg')
    print(get_bird_box('./test.jpg'))
    cropped = ci.crop_and_process(img, get_bird_box('./images/ducks.jpg'))
    for img in cropped:
        print(what_bird(img))
       


if __name__ == "__main__":
    main()