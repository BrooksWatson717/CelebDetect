import wikipedia
import photos
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='f0e6fc3d957149a8888c178d77760878')
model = app.models.get('celeb-v1.3')
response = model.predict_by_filename('/Users/brooks/Desktop/IMG_2104.jpg')

w = response['outputs']
print('********************************')
print('The celebrity is: ')
item = w[0]['data']['regions'][0]['data']['concepts'][0]['name']
print(item)
print()
print()
celebInfo = wikipedia.summary(item)
print(celebInfo)
