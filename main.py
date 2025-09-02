def main():
    import requests
    link = "https://www.codewars.com/dashboard"

    responce = requests.get(link)

    status = responce.status_code
    if status:
        with open('content.html', 'w', encoding='utf-8') as file:
            file.write(responce.text)
    else:
        return status

if __name__ == '__main__':
    if main() == None:
        print('Пошел наху')
    else:
        print(main())