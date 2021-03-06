from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
from gtts import gTTS
import os

def authenticator():
    apikey = #write your ibm api key here'
    url = 'ibm url here'
    # Setup Service
    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

def given_string_to_audio_ibm_watson(string):
    authenticator()
    with open('./speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(string, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)
    return playsound('./speech.mp3')

def given_string_to_audio_gtts(string):
    language = 'en'
    myobj = gTTS(text=string, lang=language, slow=False)
    myobj.save("speech.mp3")
    return playsound('./speech.mp3')
