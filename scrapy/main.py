import requests
from bs4 import BeautifulSoup
import json
import fake_useragent
import shutil
import os

number_page = 15
image_number = 1
for page in range(2):

    link = f'https://books.toscrape.com/catalogue/page-{number_page}.html'

    responce = requests.get(link)
    soup = BeautifulSoup(responce.text, 'lxml')

    block_main = soup.find('div', class_='col-sm-8 col-md-9')
    section = block_main.find('section')
    two_div = section.find_all('div')[1]
    li_all = two_div.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for li in li_all:
        product_pod = li.find('article', class_="product_pod")
        block = product_pod.find('div', class_="image_container")
        a_link = block.find('a').get('href')

        total_link = f'https://books.toscrape.com/catalogue/{a_link}'
        responce = requests.get(total_link)

        soup_result = BeautifulSoup(responce.text, 'lxml')

        with open('../pages/books.html', 'w', encoding='utf-8') as file:
            file.write(soup_result.text)

        # Find img url
        product_gallery = soup_result.find('div', id="product_gallery")

        thumbnail = product_gallery.find('div', class_="thumbnail")
        block = thumbnail.find('div', class_="carousel-inner")
        block_img = block.find('div', class_="item active")
        
        download_img = block_img.find('img').get('src')
        total_download = f'https://books.toscrape.com/{download_img[6:]}'
        
        img_reposnce = requests.get(total_download).content

        with open(f'../img/{image_number}.jpg', 'wb') as file:
            file.write(img_reposnce)
        image_number += 1
        number_page += 1