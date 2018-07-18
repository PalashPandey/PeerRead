import os
import json 
from pprint import pprint
import nltk
from nltk.sentiment.util import * 
import sys
import io

old_stdout = sys.stdout # Memorize the default stdout stream
sys.stdout = buffer = io.StringIO()
 	
sentDict = {}
result_string = ''
sentNumericResult = 0 
for filename in os.listdir(os.getcwd()):
	# print(filename)
	if filename == 'jsonParse.py' :
		pass
	elif filename == 'genderClassification.py' :
		pass
	elif filename == 'sentiment_result.txt' :
		pass

	else:		
		with open(filename) as f:
			data = json.loads(f.read())
			finalDictResult = 0
			for i in data['reviews']:
				pprint(i['comments'])
				# print(nltk.sentiment.util.demo_liu_hu_lexicon(i['comments'], plot=True))
				nltk.sentiment.util.demo_liu_hu_lexicon(i['comments'], plot=False)
				sys.stdout = old_stdout
				whats_printed = buffer.getvalue()
				result_string += whats_printed
				sentResult = whats_printed
				# print(whats_printed)

				# print(sentResult)
				# sentNumericResult = 0 
				if sentResult == 'Positive':
					# sentNumericResult = 1
					# print('Positive asdasdas')
					sentNumericResult += 1
				if sentResult == 'Negative':
					sentNumericResult += -1
					# print('Negative')
				if sentResult == 'Neutral':
					sentNumericResult += 0
					# print(Neutral)
				# sentDict[filename] += finalDictResult
				finalDictResult += sentNumericResult
				# print(filename, finalDictResult)
				if filename in sentDict:
					sentDict[filename] += finalDictResult
				else:
					sentDict[filename] = finalDictResult
				# pprint(sentDict)
				# print()
				# print()
				# print()
				# print()
result_file = open('sentiment_result.txt', 'w+')
result_file.write(result_string)
result_file.close()

pprint(sentDict)