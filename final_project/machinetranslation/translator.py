import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

'''
Creates Translator instance 
Translates English to Frech
Translates French to English

'''

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('waMUEBPyK9uSrKSxCdcZRGyNv7DMSMQbTATTF3lYLKIV')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/1a0e246a-75ce-49b5-83bd-6b17278495bc')

'''
The function takes english text as input
Returns french text
Uses translate function from watson
'''
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text, model_id = 'en-fr').get_result()
    french_text = translation['translation'][0]['translation']
    return french_text

'''
The function takes french text as input
Returns English text
Uses translate function from watson

'''
def french_to_english(french_text):
    translation = language_translator.translate(text = french_text, model_id = 'fr-en').get_result()
    english_text = translation['translation'][0]['translation']
    return english_text