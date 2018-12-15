"""
This script is intended to be used to scrap all products images available on Open Food Facts.

Images will be stored in [project]/data/images/
"""

import urllib
from os.path import join, exists
from os import mkdir

import numpy as np
import pandas as pd

from healthy_candies.load import load_data
from healthy_candies.load.schema import SCHEMA
from healthy_candies.path import DATA_FOLDER

if __name__ == '__main__':
    IMAGES_FOLDER = join(DATA_FOLDER, 'images')
    if not exists(IMAGES_FOLDER):
        mkdir(IMAGES_FOLDER)

    # We scrap the small sized images
    cols = ['code', 'image_small_url']
    df = load_data(cols, False)
    df = df.fillna('')
    interesting = df[df.image_small_url != '']

    for i, r in interesting.iterrows():
        # Images are stored on OFF according to their code
        code = r.code
        image_url = r.image_small_url
        ext = image_url.split('.')[-1]
        destination = join(IMAGES_FOLDER, code + '.' + ext)
        urllib.request.urlretrieve(image_url, destination)
