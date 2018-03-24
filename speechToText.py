# transcribes a YouTube video using IBM Watson

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

inputPath = raw_input('Input file path: ')

speech_to_text = SpeechToTextV1(
    username='6c563b7e-ad7a-4d19-936b-b752bab59b47',
    password='nLEwR2QX1QBI',
    url='https://stream.watsonplatform.net/speech-to-text/api')

#print(json.dumps(speech_to_text.list_models(), indent=2))

#print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), inputPath),
          'rb') as audio_file:
    print(
        json.dumps(
            speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/wav',
                timestamps=True,
                word_confidence=True),
            indent=2))

