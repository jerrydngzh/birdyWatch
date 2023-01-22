from './objectDetection/testing.py' import crop_all
from './objectDetection/testing.py' import get_bird_box
from './objectDetection/testing.py' import what_bird
from './descriptionParsing/nameToParsedWikiArticle.py' import nameToParsedWikiArticle

def make_img(img):
    """
    takes in image and returns a list of cropped images
    :param img: image to crop
    :return: list of cropped images
    """