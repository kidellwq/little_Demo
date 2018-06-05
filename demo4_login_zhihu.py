import time

import requests
from bs4 import BeautifulSoup

session = requests.Session()

i1 = session.get(
    url='https://www.zhihu.com/signin',
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.'
                      '2883.87 Safari/537.36',
    }
)

print(i1.text)