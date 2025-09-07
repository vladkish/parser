import requests
from bs4 import BeautifulSoup
import json
import fake_useragent
import shutil
import os

image_number = 1
storage_page = 1
for storage in range(50):

    link = f"https://books.toscrape.com/catalogue/page-{storage_page}.html"
    
    responce = requests.get(link)

    soup = BeautifulSoup(responce.text, 'lxml')

    main_block = soup.find('div', class_="col-sm-8 col-md-9")
    section = main_block.find('section')
    div_row = section.find_all('div')[1]
    ol = div_row.find('ol', class_="row")

    # All books from first page
    images = ol.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for image in images:
        block = image.find('div', class_="image_container")
        a_link = block.find('a').get('href')
        donwload_image = f'https://books.toscrape.com/catalogue/{a_link}'

        # responce
        page = requests.get(donwload_image)
        donwload = BeautifulSoup(page.text, 'lxml')

        main_block = donwload.find('div', class_="col-sm-6")
        carousel_inner = main_block.find('div', class_="carousel-inner")
        item_active = carousel_inner.find('div', class_="item active")
        img = item_active.find('img').get('src')

        link_download = f'https://books.toscrape.com/{img[6:]}'
        bytes_image = requests.get(link_download).content
        
        with open(f'../img/{image_number}.jpg', 'wb') as file:
            file.write(bytes_image)
            image_number += 1
        
        print('img donwload', image_number)
    storage_page += 1