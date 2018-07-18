from genderize import Genderize 
# from gender import getGenders
import gender_guesser.detector as gender
import os
import json 
from pprint import pprint
import nltk
from nltk.sentiment.util import * 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import codecs
analyzer = SentimentIntensityAnalyzer()
result_string = ''
sent_dict = {}
api_counter = 0
# comp_score = 0
for filename in os.listdir(os.getcwd()):
	print(filename)
	if filename == 'jsonParse.py' or filename == 'genderClassification.py' or filename == 'sentiment_result.txt' or filename == 'sent_class.py' or filename == 'para_class.py' or filename == 'emoji_utf8_lexicon.txt'or filename == 'vaderTest.py' or filename == 'vader_lexicon.txt' or filename == 'sent_dict.json' or filename == 'sentiment_gender.csv' or filename == 'sentiment_gender.xlsx'  :
		pass
	else:		
		with open(filename) as f:
			data = json.loads(f.read())
			authors = data['authors']
			paper_title = data['title']
			authorsList = authors.split(',')
			author_gender_list = []

			print(authorsList)
			for j in authorsList:
				j = j.strip()
				firstname_list = []
				firstname_list.append(j.split()[0])
				first_name = str(j.split()[0])
				gender_clasifier = gender.Detector()
				api_counter += 1
				# author_gender = gender_clasifier.get_gender(first_name )
				# author_gender_list.append('Male')   
				author_gender_list.append(Genderize().get(firstname_list)[0]['gender'])
			
			for i in data['reviews']:
				comp_total = 0	
				# print(i)
				# try:
					# if i['TITLE'] == 'ICLR committee final decision':
				for lines in nltk.sent_tokenize(i['comments']):
					# print(i)
					vs = analyzer.polarity_scores(lines)
					comp_score = vs['compound']
					# print('Comp_score' + str(comp_score))
					# print()
					# print()
					comp_total += comp_score
						
				# except:
				# 	pass
						# print(lines)
					# print()
					# print()
				# print('************************************************')
				# print(comp_total)
				# result_string += (str(i) + '/n' + str(comp_total))
				# for i in data['reviews']:
				# print('Comp_total *************************************' + str(comp_total))
				sent_dict[i['comments']] = [comp_total , (data['accepted']) , author_gender_list, paper_title ]
				
		# for i in authorsList:
		# 	print(i.strip())
		# 	firstname= i.split()[0]
		# 	firstname_list = []
		# 	firstname_list.append(firstname)
		# 	# firstname_list.append(lastname)
		# 	print(firstname)
		# 	print(firstname_list)
		# 	# print((Genderize().get(str(firstname))[1]['gender']))
		# 	print(Genderize().get(firstname_list))

result_file = open('sentiment_result.txt', 'w+')
result_file.write(json.dumps(sent_dict))
result_file.close()
print('API counter  ' + str(api_counter))
# pprint(sent_dict)

with open('sent_dict.json', 'w+') as fp:
	json.dump(sent_dict, fp, sort_keys=True, indent= 4)

csvFile = open('sentiment_gender.csv' , 'w+', encoding='utf-8')

csvHeader = 'comment, title,  sentiment_score, acceptance, gender \n '
csvFile.write(csvHeader)
for i in sent_dict:
	csvFile.write( i.replace(',' , '').replace('\n' , '') + ',' + sent_dict[i][3] + ',' + str(sent_dict[i][0]) + ',' +  str(sent_dict[i][1]) + ',' + str(sent_dict[i][2]).replace(',' , '')  + '\n')
csvFile.close()
