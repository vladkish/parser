import requests 
from bs4 import BeautifulSoup

'''
Fnc - display realy user-agent script
'''

def display_user_agent(headers):
    link = 'https://www.whatismybrowser.com/?utm_source=chatgpt.com'

    responce = requests.get(link, headers=headers)

    soup = BeautifulSoup(responce.text, 'lxml')

    # Fing ip
    block = soup.find('div', id = "readout-quinary")

    if not block == None:
        ip_from_a = block.find('a', class_="user_agent").text
    else:
        return None

    try:
        return ip_from_a
    except:
        return