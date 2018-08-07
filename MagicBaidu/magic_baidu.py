import os
import random
import time

import cchardet
import requests

from bs4 import BeautifulSoup
from MagicBaidu.config import USER_AGENT


class MagicBaidu():
	"""
	Magic baidu search.
	"""

	def __init__(self):
		pass

	def search(self, query, start=0, pause=2):
		"""
		Get the results you want,such as title,description,url
		:param query:
		:param start:
		:return: Generator
		"""
		start = start // 10 * 10
		content = self.search_page(query, start, pause)
		soup = BeautifulSoup(content, "html.parser")
		now = start + 1
		for item in soup.find_all('div'):
			if item.has_attr('id') and item['id'] == str(now):
				now += 1
				result = {}
				result['title'] = item.h3.get_text()
				result['url'] = item.h3.a['href']
				ss = ''
				for div in item.find_all('div'):
					if div.has_attr('class') and (div['class'][0].find('abstract') != -1 or div['class'][0] == 'c-row'):
						ss += div.get_text()
				result['text'] = ss
				yield result

	def search_page(self, query, start=0, pause=2):
		"""
		Baidu search
		:param query: Keyword
		:param language: Language
		:return: result
		"""
		start = start // 10 * 10
		time.sleep(pause)
		param = { 'wd' : query , 'pn': str(start) }
		url = 'https://www.baidu.com/s'
		# Add headers
		headers = { 'user-agent': self.get_random_user_agent(), 
					'host': 'www.baidu.com',
					'referer': 'https://www.baidu.com/s',
					'is_referer': 'https://www.baidu.com/s'
					}
		try:
			requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
			r = requests.get(url=url,
							 params=param,
							 headers=headers,
							 allow_redirects=False,
							 verify=False,
							 timeout=10)
			content = r.content
			charset = cchardet.detect(content)
			text = content.decode(charset['encoding'])
			return text
		except:
			return None

	def search_url(self, query, start=0, pause=2):
		"""
		:param query:
		:param start:
		:return: Generator
		"""
		start = start // 10 * 10
		content = self.search_page(query, start, pause)
		soup = BeautifulSoup(content, "html.parser")
		now = start + 1
		for item in soup.find_all('div'):
			if item.has_attr('id') and item['id'] == str(now):
				now += 1
				yield item.h3.a['href']

	def pq_html(self, content):
		"""
		Parsing HTML by pyquery
		:param content: HTML content
		:return:
		"""
		return pq(content)

	def get_random_user_agent(self):
		"""
		Get a random user agent string.
		:return: Random user agent string.
		"""
		return random.choice(self.get_data('user_agents.txt', USER_AGENT))

	def get_data(self, filename, default=''):
		"""
		Get data from a file
		:param filename: filename
		:param default: default value
		:return: data
		"""
		root_folder = os.path.dirname(__file__)
		user_agents_file = os.path.join(
			os.path.join(root_folder, 'data'), filename)
		try:
			with open(user_agents_file) as fp:
				data = [_.strip() for _ in fp.readlines()]
		except:
			data = [default]
		return data

	def get_real_url(self, url, pause=0.1):
		time.sleep(pause)
		headers = { 'user-agent': self.get_random_user_agent(), 
					'host': 'www.baidu.com',
					'referer': 'https://www.baidu.com/s',
					'is_referer': 'https://www.baidu.com/s'
					}
		for _ in range(3):
			try:
				requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
				r = requests.get(url=url,
								 headers=headers,
								 allow_redirects=False,
								 verify=False,
								 timeout=_+1)
				return r.headers['Location']
			except:
				time.sleep(0.5)
		return url
		