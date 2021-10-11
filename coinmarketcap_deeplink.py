import urllib.request
import os 
import time

import pandas 

if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")

df = pandas.read_csv("parsed_files/coinmarketcap_dataset.csv")

print(df)

link = "/currencies/bitcoin/"
file_name = link.replace("/currencies/", "").replace("/","")
print(file_name)
f = open("deep_link_html/coinmarketcap" + file_name + ".html", "wb")
response = urllib.request.urlopen("https://coinmarketcap.com/" + link) 
html = response.read()
f.write(html)
f.close()
