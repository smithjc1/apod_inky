#!/usr/bin/env python3

import sys
import json
import requests
import urllib.request
from PIL import Image
from inky.auto import auto
from datetime import datetime


def pull_image():
    api_key=""
    api_base="https://api.nasa.gov/planetary/apod"
    response = requests.get(api_base+"?api_key="+api_key)
    image_url = response.json()['hdurl']
    print(image_url)
    urllib.request.urlretrieve(image_url, "daily")
    write_image("daily")


def write_image(image_path):
    inky = auto(ask_user=True, verbose=True)
    saturation = 0.5

    image = Image.open(image_path)
    resizedimage = image.resize(inky.resolution)

    if len(sys.argv) > 2:
        saturation = float(sys.argv[2])

    inky.set_image(resizedimage, saturation=saturation)
    inky.show()

pull_image()
