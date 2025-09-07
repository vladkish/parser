import requests
from bs4 import BeautifulSoup
import fake_useragent
import json

def github_projects():

    session = requests.Session()

    link = 'https://streetwear.com.ua/user/login'

    data = {
        'LoginForm[login]' : 'private_data',
        'LoginForm[password]' : 'private_data'
    }

    headers = {
        'user-agent' : fake_useragent.UserAgent().random
    }
    
    responce = session.post(link, headers=headers, data=data)

    # Save cookies first session.
    cookies_dict = []
    for cookie in session.cookies:
        cookies_info = {
            'domain' : cookie.domain, 
            'name' : cookie.name, 
            'path' : cookie.path,
            'value' : cookie.value
        }
        cookies_dict.append(cookies_info)

    if responce.status_code == 200:
        link = 'https://streetwear.com.ua/favorite'

        session2 = requests.Session()
        for cookie in cookies_dict:
            session2.cookies.set(**cookie)

        profile = session2.get(link, headers=headers)

        with open('../pages/profile.html', 'w', encoding='utf-8') as file:
            file.write(profile.text)

        # try:
        context = {}

        soup = BeautifulSoup(profile.text, 'lxml')

        # Find blocks about products
        section = soup.find('section', class_="section")
        products_layout = section.find('div', class_="products-layout grid")
        blocks = products_layout.find_all('div', class_="product-item")

        if blocks:
            for index, block in enumerate(blocks, start=1):
                '''
                block == class(product-item)
                ''' 
                # product
                product = block.find('div', class_="product")

                # media
                try:
                    media = product.find('div', class_="entry-media")
                    a_media = media.find('a', class_="entry-url")

                    url_media = a_media.find('img', class_="thumb").get('src')

                    if f'product{index}' not in context:
                        context[f'product{index}'] = {}
                    context[f'product{index}']['media'] = f"https://streetwear.com.ua{url_media}"

                    try:
                        # size
                        hover = media.find('div', class_="hover")
                        entry_sizes = hover.find('div', class_="entry-sizes").text

                        # sale
                        status_sale = media.find('div', class_="status-sale").text

                        context[f'product{index}']['size'] = entry_sizes
                        context[f'product{index}']['sale'] = status_sale
                    except:
                        # size
                        hover = media.find('div', class_="hover")
                        entry_sizes = hover.find('div', class_="entry-sizes").text

                        context[f'product{index}']['size'] = entry_sizes

                except Exception as e:
                    return "Don't save media", e
                                
                # title and price
                try:
                    product = block.find('div', class_="product")
                    entry_main = product.find('div', class_="entry-main")

                    # scrapy title
                    title = entry_main.find('p', class_='entry-title')
                    a_title = title.find('a').text
                    context[f'product{index}']['title'] = a_title

                    # scrapy price
                    entry_price = entry_main.find('p', class_="entry-price")

                    try:
                        del_price = entry_price.find('del').text
                        span_price = entry_price.find('span', class_="price").text

                        context[f'product{index}']['price'] = span_price
                        context[f'product{index}']['del_price'] = del_price

                    except:
                        span_price = entry_price.find('span', class_="price").text
                        context[f'product{index}']['price'] = span_price

                except Exception as e:
                    return "Don't save title and price"

            with open("products.json", "w", encoding="utf-8") as f:
                json.dump(context, f, ensure_ascii=False, indent=4)
        else:
            return "None blocks with products"
        
    else:
        return responce.status_code

    
print(github_projects())