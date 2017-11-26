import pandas as pd, scipy as sp, numpy as np, seaborn as sb, requests as req, re

def scrape(url):
	page = requests.get(url)

	# regex = "[0-9]+\.\d\d"
	# prices = re.findall(regex,str(page.content))

	# print(str(page.content))
	# for price in prices:
		# print(prices.index(price),price)

	# Find the URLy things based on the pattern we see. 
	regex = "/ip/[A-Za-z0-9\-]+/[A-Za-z0-9\-]+"
	urls = re.findall(regex,str(page.content))

	# Iterate through the links to see the first instance of each link. Reduce index size to all unique links.
	maximum = -1 # maximum index 
	for urli in range(0,len(urls)-1):
		url = urls[urli]
		if urls.index(url) > maximum:
			maximum = urls.index(url)

	url_branches = []

	# Iterate through unique links and add to new list.
	for i in range(0,maximum):
		subdir = 'https://www.walmart.com'+urls[i]
		# print(subdir)
		url_branches.append(subdir)

	combos = []
	for url in url_branches:
		combos.append(subdirscrape_walmart(url))