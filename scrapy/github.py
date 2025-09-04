import requests
from bs4 import BeautifulSoup
import fake_useragent

def github_projects(username):

    link = f'https://github.com/{username}?tab=repositories'

    headers = {
        'user-agent' : fake_useragent.UserAgent().random
    }

    responce = requests.get(link, headers=headers)

    try:

        context = {}

        with open('../pages/project.html', 'w', encoding='utf-8') as file:
            file.write(responce.text)

            soup = BeautifulSoup(responce.text, 'lxml')
            block = soup.find('div', id = "user-repositories-list")
            block_ul = block.find_all('div', class_="d-inline-block mb-1")

            try:
                for content in block_ul:
                    text = content.find('h3', class_='wb-break-all')
                    link_on_the_project = text.find('a')
                
                    context[link_on_the_project.text.replace('\n', '').replace(' ', '')] = f'https://github.com{link_on_the_project.get('href')}'
                return context
            except:
                return "Error"

    except:
        if responce.text.lower() == "not found":
            return "Don't have user"

print(github_projects(input('enter username user from github - > ')))