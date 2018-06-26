#! /usr/bin/python

import os
from google.cloud import storage
#upload blob to gs from local
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

