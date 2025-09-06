import requests
from bs4 import BeautifulSoup
import fake_useragent

def github_projects():

    session = requests.Session()

    link = 'https://streetwear.com.ua/user/login'

    data = {
        'LoginForm[login]' : 'kishkovarv@gmail.com',
        'LoginForm[password]' : 'Kish2008V'
    }

    headers = {
        'user-agent' : fake_useragent.UserAgent().random
    }
    
    responce = session.post(link, headers=headers, data=data)

    if responce.status_code == 200:
        return responce.text
    else:
        return responce.status_code
    
print(github_projects())