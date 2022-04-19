from pyunsplash import PyUnsplash
import requests
import random
import os


# Gets a random image using random word in below array
def get_image(imgtitle):

    cars = ["sky", "cloud", "background"]

    ACCESS_KEY = os.environ['ACCESS_KEY']

    # instantiate PyUnsplash object
    pu = PyUnsplash(api_key= ACCESS_KEY)


    # Get's random query from array
    num = random.randint(0,1)

    #Featured true gives me less values to work with
    photos = pu.photos(type_='random', count=1, featured=False, query=cars[num])
    [photo] = photos.entries
    print(photo.id, photo.link_download)

    response = requests.get(photo.link_download, allow_redirects=True)
    open('./working/' + imgtitle + '.png', 'wb').write(response.content)



