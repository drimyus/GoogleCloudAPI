import base64
import json
import requests


class VisionUtils:
    def __init__(self):
        self.endpoint_url = 'https://vision.googleapis.com/v1/images:annotate'
        self.api_key = 'AIzaSyCSqfhtZXwEy8JxJRtUYm31YWLC1aACUMg'

    def __make_request(self, img_path, feature_type):
        request_list = []

        # Read the image and convert to json
        with open(img_path, 'rb') as img_file:
            content_json_obj = {'content': base64.b64encode(img_file.read()).decode('UTF-8')}

            feature_json_obj = [{'type': feature_type}]

            request_list.append(
                {'image': content_json_obj,
                 'features': feature_json_obj}
            )

        # Write the object to a file, as json
        # output_filename = 'request.json'
        # with open(output_filename, 'w') as output_json:
        #     json.dump({'requests': request_list}, output_json)

        return json.dumps({'requests': request_list}).encode()

    def __get_response(self, json_data, info_field):
        response = requests.post(
            url=self.endpoint_url,
            data=json_data,
            params={'key': self.api_key},
            headers={'Content-Type': 'application/json'})

        print(response)
        ret_json = json.loads(response.text)
        try:
            return ret_json['responses'][0][info_field]
        except:
            return None

    def detect_text(self, path, type):
        if type == 'text':
            ret_json = self.__get_response(self.__make_request(img_path=path, feature_type='TEXT_DETECTION'),
                                           info_field='textAnnotations')
        elif type == 'label':
            ret_json = self.__get_response(self.__make_request(img_path=path, feature_type='LABEL_DETECTION'),
                                           info_field='labelAnnotations')

        return ret_json

if __name__ == '__main__':

    vision = VisionUtils()

    result = vision.detect_text('image.jpg', 'label')

    print(result)
