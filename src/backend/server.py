from flask import Flask, request, send_from_directory
from imageProcessor import make_birds
import json

app = Flask(__name__)

# what it's supposed to be like:
# 1. POST -- FE sends request w/ image body, respond with fully formed data

    # a. POST -- google cloud -> response img w/ bounding box, & cropped

    # b. call tensorflow library -> label image, determine bird species

    # c. GET -- call wiki -> get flavour text

    # d. send back to FE as response -> flavour text / image labeled data as json string

@app.route("/whosThatBirdmon", methods = ['POST'])
def whosThatBirdmon():
    print("in whosThatBirdmon fxn")
    requestObj = request.json
    # deserialize json request object
    base64String = requestObj['birdBase64']

    # decode base64 string to image, save to local file system
    import base64
    base64ImageBytes = base64String.replace('data:image/png;base64,', '').encode()
    imageFilePath = f"src/backend/objectDetection/images/bird.png"
    
    with open(imageFilePath, "wb") as fh:
        fh.write(base64.decodebytes(base64ImageBytes))

    # get image file path from local file system
    ImageLabeledBirdsList = make_birds(imageFilePath)

    if (len(ImageLabeledBirdsList) == 0):
        return []

    print(ImageLabeledBirdsList[0])

    # serialize ImageLabeled Class
    birdsDict = {
        "birds": []
    }
    for bird in ImageLabeledBirdsList:
        birdsDict["birds"].append({
            "name": bird.scientific_name,
            "bbox": bird.bounding_box,
        })

    # bird.image = bird.image.decode("utf-8")
    response = json.dumps(birdsDict)

    return response


# @app.route("/")
# def base():
#     return "base of the flask server"

#serve static folder
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../frontend', path)


if __name__ == "__main__":
    app.run()