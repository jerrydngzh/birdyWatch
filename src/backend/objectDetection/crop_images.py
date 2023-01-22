from PIL import Image
import numpy as np


def crop_and_process(img, edges):
    """

    :param img: single image to process
    :param edges: list of bounded box edges
    :return: np arrays of cropped and processed imgs
    """
    edges = get_pixel_pos(img, edges)
    crop_imgs = crop_image(img, edges)
    arrs = []
    for i in range(len(crop_imgs)):
        arrs.append(process_image(crop_imgs[i]))
    return arrs


def crop_image(img, edges):
    """
    crops image for given edges
    :param img: image to crop
    :param edges: list of 4-tuples
    :return: cropped image(s)
    """
    images = []
    for i in range(len(edges)):
        im_crop = img.crop(edges[i])
        images.append(im_crop)
    return images


# this one might be useless idk
def crop_all(images, edges):
    """
    crops all images to only bird pictures
    :param images: array of images
    :param edges: 2D array of edge tuples
    :return: 2D array of cropped images
    """
    cropped_imgs = []
    for i in range(len(images)):
        cropped_imgs.append(crop_image(images[i], edges[i]))
    return cropped_imgs


def get_pixel_pos(im, edges):
    """
    converts decimal edges to pixel edges
    for one given image
    :param edges: array of 4-tuples
    :return: array of 4-tuples as pixel values
    """
    pixel_edges = []
    for i in range(len(edges)):
        edge = (int(np.ceil(edges[i][0] * im.width)),
                int(np.ceil(edges[i][1] * im.height)),
                int(np.floor(edges[i][2] * im.width)),
                int(np.floor(edges[i][3] * im.height)))
        pixel_edges.append(edge)
    return pixel_edges


def process_image(img):
    """
    process image to fit tf requirements
    :param img: image to process
    :return: processed image as array
    """
    img = img.resize((224, 224))
    im_arr = np.array(img)
    im_arr = im_arr.astype('float32')
    im_arr /= 255.0  # set colour channels to [0,1]
    # print(im_arr)
    return im_arr


def main():
    # testing here. we'll crop for each
    # images = [Image.open(r'src/backend/objectDetection/ducks.jpg'), Image.open(r'src/backend/objectDetection/test.jpg')]
    # crop_imgs = crop_all(images, [[(475, 130, 575, 230)], edges])
    # for im in crop_imgs:
    #     for i in range(len(im)):
    #         im[i].show()
    im = Image.open(r'src/backend/objectDetection/test.jpg')
    edges = [(0.3382185995578766, 0.07789109647274017, 0.5549115538597107, 0.5403065085411072),
             (0.8049169182777405, 0.19893230497837067, 0.9949325919151306, 0.6618878841400146),
             (0.05395161733031273, 0.334568589925766, 0.2764419615268707, 0.7562070488929749)]
    # edges given in [0,1] from get_bird_box()
    print(crop_and_process(im, edges))


if __name__ == "__main__":
    main()
