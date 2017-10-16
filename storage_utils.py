import json
import os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../static/service_account_key.json'
os.environ['GOOGLE_PRODUCT'] = 'ocr engine'

BUCKET_NAME = 'bill_files_test'


class GoogleStorageAPI:

    def __init__(self):
        pass
        # self.credentials = GoogleCredentials.get_application_default()
        # self.storage = discovery.build('storage', 'v1', credentials=self.credentials)

    # Define a function to download the blob from GCS to local destination
    def download_blob(self, bucket_name, source_blob_name, destination_file_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print('Blob {} downloaded to {}.'.format(source_blob_name, destination_file_name))

    def get_list_bucket(self, bucket_name, source_blob_name, destination_file_name):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print('Blob {} downloaded to {}.'.format(source_blob_name, destination_file_name))

if __name__ == '__main__':
    gcs = GoogleStorageAPI()
    gcs.download_blob(BUCKET_NAME, 'EDP1.JPG', 'EDP1.JPG')
    # gcs.get_bucket(BUCKET_NAME)
