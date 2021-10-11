from bs4 import BeautifulSoup
import pandas

import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


df = pandas.DataFrame()

for file_name in glob.glob("html_files/*.html"):
	# file_name = "html_files/coinmarketcap20211011123816.html"
	scrape_time = os.path.basename(file_name).replace("coinmarketcap", "").replace(".html", "")

	f = open(file_name, "r")
	# file_content = f.read()
	# print(file_content)

	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()


	tbody = (soup.find("tbody"))
	currency_rows = tbody.find_all("tr")

	# currency_row = currency_rows[0]
	# print(currency_row)

	for currency_row in currency_rows:
		currency_columns = currency_row.find_all("td")
		if len(currency_columns)>5:
			# print(scrape_time)
			currency_name = currency_columns[2].find("p").text
			currency_price = currency_columns[3].find("a").text.replace("$", "").replace(",", "")
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_marketcap = currency_columns[6].find("p").find("span", {"class": "sc-1ow4cwt-1"}).text.replace("$", "").replace(",", "")
			currency_link = currency_columns[2].find("a")["href"]
			currency_image = currency_columns[2].find("img")["src"]

			df = df.append({
				'time': scrape_time,
				'name': currency_name,
				'price': currency_price,
				'symbol': currency_symbol,
				'marketcap': currency_marketcap,
				'link': currency_link,
				'image': currency_image
				}, ignore_index = True) 

			
df.to_csv("parsed_files/coinmarketcap_dataset.csv")

