# transcribes a YouTube video using IBM Watson Speech-To-Text, then categorizes it using 
# Watson natural language understanding

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, CategoriesOptions


inputPath = raw_input('Input file path: ')

# credentials
speech_to_text = SpeechToTextV1(
    username='6c563b7e-ad7a-4d19-936b-b752bab59b47',
    password='nLEwR2QX1QBI',
    url='https://stream.watsonplatform.net/speech-to-text/api')

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='6e3f2109-ef69-4616-bd7e-fb34b7163fa5',
  password='L6jdLKDF2Toj',
  version='2018-03-16')

# writes the audio transcript to 'sttOutput.json'
outputData = open("sttOutput.json", 'w')

with open(join(dirname(__file__), inputPath),
          'rb') as audio_file:
    outputData.write(
        json.dumps(
            speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/wav',
                timestamps=True,
                word_confidence=True),
            indent=2))
    outputData.close()

# parses through the json file and outputs the transcript to 'transFile.txt'
outputData2 = open('sttOutput.json', 'r')
outputDic = json.load(outputData2)
transFile = open('sttFile.txt', 'w')
for k1 in outputDic['results']:
    for k2 in k1['alternatives']:
        transData = k2.get('transcript')
        transFile.write(transData)

# Watson NLP category
response = natural_language_understanding.analyze(
  text=transData,
  features=Features(
    categories=CategoriesOptions()))

# writes category to 'audioCat.json'
outputCat = open('audioCat.json', 'w')
outputCat.write(json.dumps(response, indent=2))
outputCat.close()

# parses through the json file and outputs the category to 'catFile.txt'
outputData3 = open('audioCat.json', 'r')
outputDic = json.load(outputData3)
catFile = open('audioCatFile.txt', 'w')
for k1 in outputDic['categories']:
    catData = k1.get('label')
    catList = str(catData).split('/')
    for word in catList:
        catFile.write(word + '\n')

    


