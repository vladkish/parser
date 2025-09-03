import requests 
from bs4 import BeautifulSoup

link = 'https://www.whatismybrowser.com/?utm_source=chatgpt.com'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

responce = requests.get(link, headers=headers)

soup = BeautifulSoup(responce.text, 'lxml')

# Fing ip
block = soup.find('div', id = "readout-quinary")

if not block == None:
    ip_from_a = block.find('a', class_="user_agent").text
else:
    print(None)


try:
    print(ip_from_a)
except:
    print(None)