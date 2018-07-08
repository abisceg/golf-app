#! /usr/bin/python

import os
from google.cloud import storage
#upload blob to gs from local
def upload_blob(bucket_name, source_file_name, destination_blob_name):

    """Uploads a file to the bucket."""
    # storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json('/home/abisceg/.config/gcloud/legacy_credentials/abisceg@gmail.com/adc.json')

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def list_blobs():
    bucket_name = 'bucket-67'
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    # storage_client = storage.Client.from_service_account_json('/home/abisceg/.config/gcloud/legacy_credentials/abisceg@gmail.com/adc.json')
    # storage_client = storage.Client.from_service_account_json('/home/abisceg/PycharmProjects/project2-new/venv/uml-advcc-project2-207700-c829dbac9a9e.json')

    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)
    return "Hello gcp World"

list_blobs()

'''
bucket_name  = 'bucket-67'
#sample files for vision api
pathtosamp = "/home/abisceg/Desktop/proj2samples/"
#strings for pretty output
str1 = "uploading below to gs bucket: "
str2 = "sourcefile: "
str3 = "blob name: "
#get filenames then upload using function above
files = [f for f in os.listdir(pathtosamp) if os.path.isfile(os.path.join(pathtosamp, f))]
for f in files:
    print(str1 + bucket_name)
    #prepare source file name for gs upload
    source_file_name = os.path.join(pathtosamp, f)
    print(str2 + source_file_name)
    #prepare destination name, not necessary but is more clear.
    destination_blob_name = f
    print(str3 + destination_blob_name)
    print('\n')
    upload_blob(bucket_name, source_file_name, destination_blob_name)

'''