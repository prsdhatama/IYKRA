try :
    from google.cloud import storage
except Exception as e:
    print('This module is not available{}'.format(e))

# Create a client object by reading the key, key should be in the same folder as this file
storage_client = storage.Client.from_service_account_json('feisty-outlet-362916-29300cba76c1.json')

# Define the bucket and file ino
BUCKET_NAME = 'fellowship7'
FOLDERNAME = 'practice-case-1'
FILENAME = 'file-in-GCP.txt'

# Create a bucket object
bucket = storage_client.get_bucket(BUCKET_NAME)

# Define the path and name of the file that'll uploaded to GCP bucket
bucketpath = '{}/{}'.format(FOLDERNAME,FILENAME)
# upload_filename ='%s/%s' % ('practice-case-1','iykra-practice-1.txt')

# Create the file following the defined path
blob = bucket.blob(bucketpath)

# Using with, to open and close the file safely within the function only
with open('uploaded-file.txt', mode= 'r') as f :
    blob.upload_from_file(f)
    
print('Upload Completed')