import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='6e3f2109-ef69-4616-bd7e-fb34b7163fa5',
  password='L6jdLKDF2Toj',
  version='2018-03-16')

outputData2 = open('output.json', 'r')
outputDic = json.load(outputData2)
transFile = open('transFile.txt', 'w')
for k1 in outputDic['results']:
    for k2 in k1['alternatives']:
        transData = k2.get('transcript')
        transFile.write(transData)

response = natural_language_understanding.analyze(
  text=transData,
  features=Features(
    categories=CategoriesOptions()))

outputCat = open('audioCat.json', 'w')
outputCat.write(json.dumps(response, indent=2))
outputCat.close()

outputData3 = open('audioCat.json', 'r')
outputDic = json.load(outputData3)
catFile = open('catFile.txt', 'w')
for k1 in outputDic['categories']:
	catData = k1.get('label')
	catList = str(catData).split('/')
	for word in catList:
		catFile.write(word + '\n')













		

		
	

