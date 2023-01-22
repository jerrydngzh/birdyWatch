# Who's That Birdymon? - Bird Watching WebApp
## nwHacks 2023 Hackathon Project 

Turn your device into a Pokedex for birds with **`Who’s that Birdymon?™`** 🐦🐓🐤🐧🦃🦅🦆🦉🕊🦢🦜🦚!

Our team developed a full-stack application that can identify birds from your camera or image upload. You just find the birds–we’ll identify their common name, scientific name, and a quick description. 

It works right through your device’s camera to capture a snapshot of any birds in the vicinity. We accept the request through our backend flask server, which passes the appropriate information to our microservices.  Using Google Cloud’s Vision API, we can identify bounding boxes on all the birds. We crop these images and send them to a TensorFlow model that classifies & labels the species of the bird in the given image. 

Once we’ve identified a bird’s species, we can use Wikipedia’s API and parse information from any given bird’s page for flavor text. All of this data is sent back to the frontend, where we display the information for all birds in the original photo sent, which means yes, our application is able to handle photos with more than one bird. With **`Who’s that Birdymon?™`**, it’s never been easier to become a Birdymon™ master. 

## Technologies Used
### Frontend:
- HTML, CSS, JS

### Backend
- Python
- Flask Server w/ REST API
- [TensorModel](https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1)
- [Google Cloud Vision API](https://cloud.google.com/vision/docs/object-localizer#vision_localize_objects-python)
- [Wikipedia API](https://pypi.org/project/wikipedia/)

### Team members: [Alex C](https://github.com/alexander-chudinov), [Jerry D](https://github.com/jerrydngzh), [Jubelle P](https://github.com/jubelle-anne), [Tayyib C](https://github.com/TayyibChohan)
