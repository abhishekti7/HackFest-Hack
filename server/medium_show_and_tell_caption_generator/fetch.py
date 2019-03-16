import firebase_admin
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import datetime
from url_download import extract
from firebase_admin import credentials
from firebase_admin import storage
cred = credentials.Certificate('serviceacckey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'eyeai-cafee.appspot.com'
})
bucket = storage.bucket()
blob = bucket.blob('t.png')
url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
extract(url)
