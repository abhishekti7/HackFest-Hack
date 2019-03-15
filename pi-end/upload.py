import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
cred = credentials.Certificate('serviceacckey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'eyeai-cafee.appspot.com'
})
bucket = storage.bucket()
blob = bucket.blob('t.png')
localpath='t.png'
blob.upload_from_filename(localpath)
