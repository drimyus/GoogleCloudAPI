#
import base64
import os
import sys
import json

from googleapiclient import discovery
from googleapiclient import errors
from oauth2client.client import GoogleCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../static/service_account_key.json'
os.environ['GOOGLE_PRODUCT'] = 'ocr engine'

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'  # noqa


class GoogleVisionAPI:
    """Construct and use the Google Vision API service."""

    def __init__(self):

        self.credentials = GoogleCredentials.get_application_default()

        self.service = discovery.build('vision', 'v1', credentials=self.credentials, discoveryServiceUrl=DISCOVERY_URL)

    def detect_text(self, input_filenames, num_retries=3, max_results=6):
        """ Uses the Vision API to detect text in the given file. """
        images = {}
        for filename in input_filenames:
            with open(filename, 'rb') as image_file:
                images[filename] = image_file.read()

        batch_request = []
        for filename in images:
            batch_request.append({
                'image': {
                    'content': base64.b64encode(images[filename]).decode('UTF-8')
                },
                'features': [
                    {
                        'type': 'DOCUMNET_TEXT_DETECTION',
                        'maxResults': max_results,
                    },
                ]
            })
        request = self.service.images().annotate(
            body={'requests': batch_request})

        try:
            responses = request.execute(num_retries=num_retries)

            print(responses)

            if 'responses' not in responses:
                return {}
            text_response = {}
            for filename, response in zip(images, responses['responses']):
                if 'error' in response:
                    print("API Error for %s: %s" % (
                            filename,
                            response['error']['message']
                            if 'message' in response['error']
                            else ''))
                    continue
                if 'textAnnotations' in response:
                    text_response[filename] = response['textAnnotations']
                else:
                    text_response[filename] = []
            return text_response
        except errors.HttpError as e:
            print("Http Error for %s: %s" % (filename, e))
        except KeyError as e2:
            print("Key error: %s" % e2)
# [END detect_text]

if __name__ == '__main__':

    vision = GoogleVisionAPI()

    """Call the Vision API on a file and index the results."""
    texts = vision.detect_text(['./test2.jpg'])  # './image.jpg', './image_.jpg',
    print(texts)
