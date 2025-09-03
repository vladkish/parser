import requests
from bs4 import BeautifulSoup

link = 'https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html'
responce = requests.get(link)

context = {

}

# Ojbect html(page)
soup = BeautifulSoup(responce.text, 'lxml')

# Find main block
block = soup.find_all('div', class_="br-pr-chr-item")[2]

# Gpu block
gpu = block.find('div')

gpu_list_for = str(gpu.text).replace(' ', '').split()

for index, value in enumerate(gpu_list_for):
    if index % 2 == 0:
        context[value] = gpu_list_for[index+1]

print(context)