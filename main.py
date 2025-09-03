import requests
from bs4 import BeautifulSoup

link = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'

responce = requests.get(link)
status = responce.status_code

soup = BeautifulSoup(responce.text, 'lxml')

main_list = {}

content = soup.find_all('div', class_="br-pr-chr-item")

if __name__ == '__main__':
    if status == 200:
        try:
            for _ in content:
                main_list[_.text[1]] = _.text
            with open('content.html', 'w', encoding='utf-8') as file:
                file.write(str(main_list).replace('\n', ''))
        except TypeError as e:
            print("Dont't true agrs", e)
    else:
        print(status)