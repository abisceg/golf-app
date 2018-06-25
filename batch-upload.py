#! /usr/bin/python
import os
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

bucket_name  = 'bucket-67'
source_file_name = '/home/abisceg/Desktop/proj2samples/wayland0.jpg'
destination_blob_name = 'wayland00.jpg'

upload_blob(bucket_name, source_file_name, destination_blob_name)
