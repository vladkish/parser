# def main():
#     import requests
#     link = "https://www.codewars.com/dashboard"

#     responce = requests.get(link)

#     status = responce.status_code
#     if status:
#         with open('content.html', 'w', encoding='utf-8') as file:
#             file.write(responce.text)
#     else:
#         return status

# if __name__ == '__main__':
#     if main() == None:
#         print('Пошел наху')
#     else:
#         print(main())

import requests

link = "https://instagram.fplv1-2.fna.fbcdn.net/v/t51.2885-19/536972176_17860875546464588_1331139665925734216_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4yMjUuYzIifQ&_nc_ht=instagram.fplv1-2.fna.fbcdn.net&_nc_cat=108&_nc_oc=Q6cZ2QHuVQxpVtK2i4Q0pXeamZ7hwdSBeSoWz4PJPgLPJJwc_kEzmXCfsF1UrbKhHHn_Njc&_nc_ohc=CnVvUXnefgYQ7kNvwGtNusI&_nc_gid=MofACTfe-FExqTMMdfNTbQ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfXOklSxfiv0p8uOyijozWo1Ghd3K9f6AvSJYBc8NOntpg&oe=68BCA1AD&_nc_sid=8b3546"
responce = requests.get(link, stream=True)

with open('default.png', 'wb') as file:
    for _ in responce.iter_content(chunk_size=8192):
        file.write(_)