import os
#Google cloud vision API detection
def get_bird_box ():
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    path = os.path.join(os.path.dirname(__file__), 'test.jpg')
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    output = []
    for object_ in objects:
        x = []
        y = []
        if object_.name == "Bird":
            for vertex in object_.bounding_poly.normalized_vertices:
                x.append(vertex.x)
                y.append(vertex.y)
            output.append((min(x), max(y), max(x), min(y)))
    return output
def main():
    print(get_bird_box())


if __name__ == "__main__":
    main()