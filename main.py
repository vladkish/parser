import requests
from bs4 import BeautifulSoup

link = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'

responce = requests.get(link)

with open('content.html', 'w', encoding='utf-8') as file:
    file.write(responce.text)

soup = BeautifulSoup(responce.text, 'lxml')

context = {}

block = soup.find('div', attrs={
    'class' : 'bg-white rounded-2 p-4'
})
print(block)