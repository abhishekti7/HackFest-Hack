import shutil
import requests
import os

def extract(url):
        # filelist = [ f for f in os.listdir(os.path.dirname()+"extracted_img/") if f.endswith(".jpeg") ]
        # for f in filelist:
        #         os.remove(os.path.join(mydir, f))   
        response = requests.get(url, stream=True)
        with open("extracted_img/img.jpeg", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

