# README #
     
### GoogleCloud Vision API ###

"""

1. Enable the 'Google Cloud Vision API'
 ./ Google Cloud Plat Form / Console / Google Cloud Vision API /
 ./ Dashboard / [Enable] set


2. API Credintial Key Generate
 1) ./ create credentials/ API key.yaml / [register] - key string
 2) ./ create credentials/ service account key / [register] - key to the [json] or [p12] 
 
 
3. Using on python 
 
 3.1
 
 Google environment value **GOOGLE_APPLICATION_CREDENTIALS**
 
  `$ export GOOGLE_APPLICATION_CREDENTIALS=/home/du/ocr_engine/googlecloudocr/static/service_account_key.json`
 
 3.2
 
 Install python library for the google cloud vision api
 
  `$ git clone https://github.com/GoogleCloudPlatform/cloud-vision.git`
  
  `$ cd cloud-vision/python/label|text`
  
  `$ sudo pip install -r requirments.txt`
  
   or `$ sudo pip install --upgrade google-cloud-vision`
 
 3.3
 
 For the Text detection(OCR), it should be needed to install some further packages
  `$ python -m nltk.downloader stopwords`
  `$ python -m nltk.downloader punkt`
  This data will be installed into a `nltk_data` directory under the home directory

  3.4
  
  In case of Anaconda
   `$ conda install -c conda-forge google-api-python-client`
   
4. Test with sample script

"""

### GoogleCloud Storage API ###
"""

1. install the needed package
 
 in case of ananconda
  
    `$ conda-forge google-cloud-storage`
 in case of python
  
    `$ sudo pip install google.cloud`

"""
### How do I get set up? ###

### Contribution guidelines ###


### Who do I talk to? ###

