#facebook scraper for DOJO NFZ

# import some Python dependencies
import urllib2
import json
import datetime
import csv
import time
import re
import pprint

access_token = ''

with open('secrets.csv','rb') as csvfile:
	readr = csv.reader(csvfile, delimiter=',')
	for x in readr:
		print x[0]
		access_token = x[0]

group_id = '688926244534060'

def getFacebookPageLinks(group_id, access_token):
	#construct the URL string
	base = "https://graph.facebook.com/v2.1"
	node = "/"+group_id+"/feed"
	parameters = "?limit=2000&access_token=%s" % access_token
	url = base +node + parameters
	print 'url:'+ url
	#retrieve data
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
    	data = json.loads(response.read())
	datastring = json.dumps(data, indent=4, sort_keys=True)	 
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', datastring)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(urls)
	with open('nfz_links.csv', 'w')  as ff:
		writr = csv.writer(ff, delimiter='\t')
		for x in urls:
			writr.writerow([x])
			print x
		
getFacebookPageLinks(group_id, access_token)

