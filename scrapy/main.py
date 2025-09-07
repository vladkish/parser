import requests
from bs4 import BeautifulSoup
import json
import fake_useragent
import shutil
import os

storage_page = 0

link = "https://books.toscrape.com/catalogue/page-1.html"
 
responce = requests.get(link)

soup = BeautifulSoup(responce.text, 'lxml')

main_block = soup.find('div', class_="col-sm-8 col-md-9")
section = main_block.find('section')
div_row = section.find_all('div')[1]
ol = div_row.find('ol', class_="row")

images = ol.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

for image in images:
    block = image.find('div', class_="image_container")
    a_link = block.find('a').get('href')
    print(f'https://books.toscrape.com/catalogue/{a_link}')