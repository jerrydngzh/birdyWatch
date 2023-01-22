from flask import Flask, redirect, url_for, request
from notMain import make_birds

app = Flask(__name__)

# what it's supposed to be like:
# 1. POST -- FE sends request w/ image body, respond with fully formed data

    # a. POST -- google cloud -> response img w/ bounding box, & cropped

    # b. call tensorflow library -> label image, determine bird species

    # c. GET -- call wiki -> get flavour text

    # d. send back to FE as response -> flavour text / image labeled data as json string

@app.route("/whosThatBirdmon", methods = ['POST'])
def whosThatBirdmon():

    # mega function that does everything
    imagePath = request.data
    ImageLabeledBirdsList = make_birds(imagePath)

    # serialize ImageLabeled Class
    response = ImageLabeledBirdsList.dumps()
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