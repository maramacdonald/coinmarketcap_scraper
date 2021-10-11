import urllib.request
import os 
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")



for i in range(5):
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time)
	f = open("html_files/coinmarketcap" + current_time + ".html", "wb")
	response = urllib.request.urlopen("https://coinmarketcap.com/")
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30)













