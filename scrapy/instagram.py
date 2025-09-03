import requests
from bs4 import BeautifulSoup
import fake_useragent
from ip_test import display_user_agent

link = 'https://www.instagram.com/vladjew/'
user = fake_useragent.UserAgent().random

headers = {'user-agent' : user}

responce = requests.get(link, headers=headers)
status = responce.status_code

if status:
    soup = BeautifulSoup(responce.text, 'lxml')


    try:
        section = soup.find('section', class_="x6s0dn4 x78zum5 xcrlgei x1cq0mwf xdx80a7 x1agbcgv xl56j7k xlo4toe x2wt2w")
        img = section.find('img', class_="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3")
        
        with open('instagram.png', 'wb') as file:
            for _ in responce.iter_content(chunk_size=8192):
                file.write(_)
    except:
        print(display_user_agent(headers), 'the problem is that instagram uses js')

else:
    print(responce.status_code)