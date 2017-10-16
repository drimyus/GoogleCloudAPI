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
        self.credentials = GoogleCredentials.get_application_default()
        self.storage = discovery.build('storage', 'v1', credentials=self.credentials)

    def get_bucket(self, bucket_name):
        # get bucket object
        request = self.storage.buckets().get(bucket=bucket_name)
        response = request.execute()

        print(json.dumps(response))

    def make_request(self):
        request = self.storage.object().list(
            bucket=BUCKET_NAME,
            fields='nextPageTokenm items(name, size, contentType, metadata(my-key))'
        )
        # Submit list requests, handling paging

        while request is not None:
            response = request.execute()
            print(json.dumps(response))
            request = storage.objects().list_next(request, response)

if __name__ == '__main__':
    gcs = GoogleStorageAPI()
    gcs.get_bucket(BUCKET_NAME)
