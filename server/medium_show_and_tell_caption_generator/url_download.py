import shutil
import requests
import os

def extract(url):
    response = requests.get(url, stream=True)
    with open("extracted_img/img.jpeg", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


        