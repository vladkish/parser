import requests
from bs4 import BeautifulSoup

link = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'

responce = requests.get(link)
soup = BeautifulSoup(responce.text, 'lxml')

content = soup.find('div', class_="br-pr-chr")
block = content.find('div', class_='br-pr-chr-item')
information_block = block.find('div')

if __name__ == '__main__':
    if responce.status_code == 200:
        try:
            print(str(information_block.contents.replace(' ', '')))
        except:
            with open('content.html', 'w', encoding='utf-8') as file:
                file.write(information_block.text.replace(' ', ''))
    else:
        print(responce.status_code)