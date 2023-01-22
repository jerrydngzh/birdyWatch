import os
import sys
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from objectDetection import crop_images as ci
from PIL import Image
import Bird as b
from  descriptionParsing import nameToParsedWikiArticle as ntp 
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\jubel\Documents\tayyib_creds.json"


# Google cloud vision API detection
def get_bird_box(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    # path = path
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


def what_bird(img):
    """
    Returns scientific name of the bird in the list of birds
    :param img: cropped image of bird
    :return: string representing bird name
    """

    bird_df = pd.read_csv(r'./aiy_birds_V1_labelmap.csv')
    m = hub.KerasLayer('https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1')
    clasifier = tf.keras.Sequential([m])
    
    out = clasifier.predict(img[np.newaxis, ...])
    # print(out)
    bird = tf.math.argmax(out[0], axis=-1).numpy()

    row = bird_df.loc[bird_df['id'] == int(bird)]
    return row.iloc[0, 1]


def make_birds(path):
    """
    returns bird info for all birds in
    image at path
    :param path:
    :return: bird information
    """
    img = Image.open(path)   
    print(get_bird_box(path))
    bounding_boxes = get_bird_box(path)
    cropped = ci.crop_and_process(img, bounding_boxes)
    birds = []
    for i in range(len(cropped)):
        scientific_name = what_bird(cropped[i])
        try:
            name = ntp.getNameFromScientificName(scientific_name)
            summary = ntp.getSummaryFromScientificName(scientific_name)
        except:
            name = "Unknown No Wikipedia Article"
            summary = "Unknown No Wikipedia Article"

        birds.append(b.Bird(name= name,
                            scientific_name=scientific_name, 
                            description=summary,
                            bounding_box=bounding_boxes[i]))
    return birds


def main():
    print(make_birds(r'./objectDetection/test.jpg'))


if __name__ == "__main__":
    main()