import os
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

FRAMES = 1000
TIMEBETWEEN = 30

cred = credentials.Certificate('serviceacckey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'eyeai-cafee.appspot.com'
})
bucket = storage.bucket()
blob = bucket.blob('t.png')
localpath='t.png'

frameCount = 0
while frameCount < FRAMES:
    os.system("raspistill -o t.png")
    frameCount += 1
    blob.upload_from_filename(localpath)
    time.sleep(TIMEBETWEEN - 30)



