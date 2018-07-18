import os
import json 
from pprint import pprint
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


for filename in os.listdir(os.getcwd()):
	print(filename)
	if filename == '1.0.py':
		pass
	else:
		
		with open(filename) as f: 
			data = json.loads(f.read())
			pprint(data['title'])
			print()
			print()
			print()
			print()
			driver = webdriver.Chrome()
			driver.implicitly_wait(10)
			driver.get('https://scholar.google.com/schhp?hl=en')
		    # Finds the search button 
			home_page = driver.window_handles[0]
			searchBar = driver.find_element_by_id('gs_hdr_tsi')
		    # Enters the user provided product name
			searchBar.send_keys(data['title'])
		    # Clicks the search button 
			# driver.implicitly_wait(10)
			# driver.find_element_by_xpath("//input[@type='submit' and @value='I'm Feeling Lucky' and @name='btnI']").click()
			# driver.find_element_by_link_text("Google Search").click()
			driver.find_element_by_id('gs_hdr_tsb').click()
			
			second_page = driver.window_handles[1]
			driver.switch_to_window(second_page)

			search = data['title']
			# driver.implicitly_wait(10) 
			# links = driver.find_elements_by_xpath("//a[@href]")
			# print(str(links))
			# links[8].click()

			driver.find_element_by_link_text(search).click()