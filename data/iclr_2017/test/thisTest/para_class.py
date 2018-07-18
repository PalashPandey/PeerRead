import os
import json 
from pprint import pprint
import nltk
from nltk.sentiment.util import * 
import sys
import io
from vaderTest import SentimentIntensityAnalyzer
import codecs 
 
analyzer = SentimentIntensityAnalyzer()
result_string = ''
sent_dict = {}
for filename in os.listdir(os.getcwd()):
	# print(filename)
	if filename == 'jsonParse.py' :
		pass
	elif filename == 'genderClassification.py' :
		pass
	elif filename == 'sentiment_result.txt' :
		pass
	elif filename == 'sent_class.py' :
		pass
	elif filename == 'para_class.py' :
		pass
	elif filename == 'vaderTest.py' :
		pass
	elif filename == 'vader_lexicon.txt' :
		pass
	elif filename == 'emoji_utf8_lexicon.txt' :
		pass

	else:		
		with open(filename) as f:
			data = json.loads(f.read())
			for i in data['reviews']:
				comp_total = 0
				# print(i)
				vs = analyzer.polarity_scores(i['comments'])
				comp_score = vs['compound']
				comp_total += comp_score
				result_string += (str(i) + '/n' + str(comp_total))
				sent_dict[i['comments']] = [comp_total , (data['accepted'])]

for i in sent_dict.values():
	# print(i)
	if i[0] > 0.5 and i[1] == False:
		# print('odd ones')
		print(i)




result_file = open('sentiment_result.txt', 'w+')
result_file.write(json.dumps(sent_dict))
result_file.close()

# pprint(sent_dict)
# sent_val_list = sent_dict.values()
# sent_val_list.sort()
# sent_val_list.reverse()

# pprint()