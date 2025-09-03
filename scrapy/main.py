import requests
from bs4 import BeautifulSoup
import json
import fake_useragent
from github import avatar_github

link = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'

# Setting headers
user = fake_useragent.UserAgent().random

headers = {
    'User-Agent' : user
}

responce = requests.get(link, headers=headers)

context = {}

# Ojbect html(page)
soup = BeautifulSoup(responce.text, 'lxml')

# Find main block
block = soup.find_all('div', class_="br-pr-chr-item")

for content in block:
    # Gpu block
    gpu = content.find('div')

    gpu_list_for = str(gpu.text).replace(' ', '').split()

    for index, value in enumerate(gpu_list_for):
        if index % 2 == 0:
            context[value] = gpu_list_for[index+1]

if __name__ == '__main__':
    try:
        with open('../main.json', 'w', encoding='utf-8') as file:
            json.dump(context, file, indent=4, ensure_ascii=False)
    except:
        print("Don't save file")

# dispaly how user-agent
print(avatar_github('AlexeyTarasov77'))