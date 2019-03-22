import wikipedia
import photos
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='f0e6fc3d957149a8888c178d77760878')
image = ClImage(
    url='https://m.media-amazon.com/images/M/MV5BMTQ1NTQwMTYxNl5BMl5BanBnXkFtZTYwMjA1MzY1._V1_UX214_CR0,0,214,317_AL_.jpg')
response = model.predict([image])


w = response['outputs']
print('********************************')
print('The celebrity is: ')
item = w[0]['data']['regions'][0]['data']['concepts'][0]['name']
print(item)
print()
print()
celebInfo = wikipedia.summary(item)
print(celebInfo)
