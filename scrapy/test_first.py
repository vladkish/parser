import requests
from bs4 import BeautifulSoup
import fake_useragent

link = 'https://brain.com.ua/api/v1/login'

session1 = requests.Session()

headers = {
    'user-agent' : fake_useragent.UserAgent().random
}

data = {
    'phone_number' : 'private_data',
    'password' : 'private_data'
}

responce = session1.post(link, headers=headers, data=data)

cookies_dict = []
for cookie in session1.cookies:
    cookies_info = {
        'domain' : cookie.domain,
        'name' : cookie.name,
        'path' : cookie.path, 
        'value' : cookie.value
    }
    cookies_dict.append(cookies_info)

# Session2
session2 = requests.Session()

for cookie in cookies_dict:
    session2.cookies.set(**cookie)

link = 'https://brain.com.ua/ukr/cabinet/'

responce = session2.get(link)

for cookie in session2.cookies:
    print(cookie)

# Ready for work