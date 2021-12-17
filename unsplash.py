from pyunsplash import PyUnsplash
import requests
import random

import os
from dotenv import load_dotenv


def get_image():
    load_dotenv()

    ACCESS_KEY = str(os.getenv('ACCESS_KEY'))

    # instantiate PyUnsplash object
    pu = PyUnsplash(api_key= ACCESS_KEY)

    cars = ["sky", "cloud", "background"]


    num = random.randint(0,2)

    #Featured true gives me less values to work with
    photos = pu.photos(type_='random', count=1, featured=False, query=cars[num])
    [photo] = photos.entries
    print(photo.id, photo.link_download)

    response = requests.get(photo.link_download, allow_redirects=True)
    open('./working/image_temp.png', 'wb').write(response.content)



