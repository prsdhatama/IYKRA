# import package safely
try:
    from google.cloud import storage
    import urllib.request
except Exception as e:
    print('This module is not available{}'.format(e))


# Create a client object by reading the key, key should be in the same folder as this file
storage_client = storage.Client.from_service_account_json('feisty-outlet-362916-29300cba76c1.json')

# Define the bucket and filename info
PROJECT_ID = 'feisty-outlet-362916'
BUCKET_NAME = 'fellowship7'
DESTINATION_FILENAME = 'file-in-GCP-frominternet.jpg'

# Define sourcefile
SOURCE_FILENAME = 'https://cdn-2.tstatic.net/tribunnews/foto/bank/images/cara-login-google-classroom-layanan-untuk-belajar-online-guru-dan-siswa-di-masa-pandemi-covid-19.jpg'

# Create a function to upload file to GCP
def upload_blob(BUCKET_NAME, SOURCE_FILENAME, DESTINATION_FILENAME):   
    # Request the file from sourcefile
    file = urllib.request.urlopen(SOURCE_FILENAME)

    # Create a bucket object
    bucket = storage_client.get_bucket(BUCKET_NAME)

    # Defining the destination filename
    blob = bucket.blob(DESTINATION_FILENAME)

    # Uploading to GCP
    blob.upload_from_string(file.read(), content_type='image/jpg')

upload_blob(BUCKET_NAME, SOURCE_FILENAME, DESTINATION_FILENAME)

print('Upload Complete')