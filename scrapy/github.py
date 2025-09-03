import requests
from bs4 import BeautifulSoup
import fake_useragent

def avatar_github(username):
    link = f"https://github.com/{username}"

    user = fake_useragent.UserAgent().firefox

    headers = {
        'user-agent' : user
    }

    responce = requests.get(link, headers=headers)
    status = responce.status_code

    if status == 200:

        try:
            with open('../content.html', 'w', encoding='utf-8') as file:
                file.write(responce.text)
        except:
            return "Don't save img"

        soup = BeautifulSoup(responce.text, 'lxml')

        block = soup.find('div', attrs={
            'class' : 'position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0'
        })

        link = block.find('a')

        # Get url avatar
        avatar = link.find('img', class_="avatar avatar-user width-full border color-bg-default").get('src')
        responce_avatar = requests.get(avatar, headers=headers)

        try:
            with open('../avatar.png', 'wb') as file:
                for _ in responce_avatar.iter_content(chunk_size=8192):
                    if _:
                        file.write(_)
        except:
            return "Don't save img"

    else:
        return status