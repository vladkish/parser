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
            with open('../user_page.html', 'w', encoding='utf-8') as file:
                file.write(responce.text)
        except:
            return "Don't save img"

        soup = BeautifulSoup(responce.text, 'lxml')

        # BlOCK LINK FROM GITHUB
        block = soup.find('div', class_="d-flex width-full position-relative")
        try:
            link_on_the_project = block.find('a', id = "853865861")

            link = f'https://github.com{link_on_the_project.get('href')}'
            responce = requests.get(link, headers=headers)

            try:
                with open('../first_project.html', 'w', encoding='utf-8') as file:
                    file.write(responce.text)
            except:
                return "Don't save file"
            
            # Creating object
            soup = BeautifulSoup(responce.text, 'lxml')
            
            try:
                block_text = soup.find('div', class_="Layout-sidebar").text

                # Filter block_text
                clean_text = block_text.strip().replace("\n", "")

                try:
                    with open('../content.html', 'w', encoding='utf-8') as file:
                        file.write(clean_text)
                except:
                    return "Don't save img"

            except AttributeError:
                block_text = soup.find('div', class_="Layout-sidebar")

            return clean_text
        
        except AttributeError as e:
            return "Don't have files", e

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

print(avatar_github('AlexeyTarasov77'))