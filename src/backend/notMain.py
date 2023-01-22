import os
import sys
import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import numpy as np
from objectDetection import crop_images as ci
from PIL import Image
import Bird as b
from  descriptionParsing import nameToParsedWikiArticle as ntp 
import pandas as pd

#Google cloud vision API detection
def get_bird_box(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    path = path
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

    bird_df = pd.read_csv(r'src\backend\aiy_birds_V1_labelmap.csv')
    m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1')
    clasifier = tf.keras.Sequential([m])
    
    out = clasifier.predict(img[np.newaxis, ...])
    # print(out)
    bird = tf.math.argmax(out[0], axis=-1).numpy()

    row = bird_df.loc[bird_df['id'] == int(bird)]
    return row.iloc[0, 1]



def make_birds(path):

    img = Image.open(path)   
    print(get_bird_box(path))
    bounding_boxes = get_bird_box(path)
    cropped = ci.crop_and_process(img, bounding_boxes)
    birds = []
    for i in range(len(cropped)):
        scientific_name = what_bird(cropped[i])
        print(scientific_name)
        # birds.append(b.Bird(name= ntp.getNameFromScientificName(scientific_name),
        #                     scientific_name=scientific_name, 
        #                     description=ntp.getSummaryFromScientificName(scientific_name),
        #                     bounding_box=bounding_boxes[i]))
    return birds

def main():
    print(make_birds(r'src\backend\objectDetection\test.jpg'))


if __name__ == "__main__":
    main()