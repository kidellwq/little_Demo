import requests
from bs4 import BeautifulSoup
import uuid

response = requests.get(
    url='https://www.autohome.com.cn/news/'
)


response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, features='html.parser')
target = soup.find(id="auto-channel-lazyload-article")
li_list = target.find_all('li')
for i in li_list:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3').text
        print(txt)
        img = 'https:'+a.find('img').attrs.get('src')
        print(img)
        img_response = requests.get(url=img)
        file_name = str(uuid.uuid4()) + '.jpg'
        with open(file_name, 'wb') as f:
            f.write(img_response.content)
