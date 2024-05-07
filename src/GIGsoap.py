import sys

import requests
from bs4 import BeautifulSoup
import time
import json

start_url = 'https://gig.ee/et/kasutatud-tehnika.html'

products = []

def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')


    brics_list = soup.find_all("li", class_='item')

    for brick in brics_list:
        try:
            data = {'name': '', 'price': '', 'picture': '', }

            data['name'] = brick.find('h2', class_='product-name').get_text()

            data['price'] = brick.find('span', class_='price').get_text().replace(u'\xa0', '').replace('\n', '').strip()

            data['picture'] = brick.find('img').get('src')

            products.append(data)
        except:
            print("Unexpected error: ", sys.exc_info()[0])

    try:
        next_page = soup.find('a', class_='next i-next').get('href')
        if next_page:
            time.sleep(5)  # to avoid http response 429
            print("----------------------------", next_page)
            parse(next_page)
    except:
        print("No more pages")

    return products

if __name__ == '__main__':
    scraped_data = parse(start_url)

    output_file = 'soap-products.json'
    with open(output_file, 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)