import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

il = requests.get('https://github.com/login')
soup = BeautifulSoup(il.text, features='html.parser')
tag = soup.find(name='input', attrs={'name': 'authenticity_token'})
authenticity_token = tag.get('value')

cl = il.cookies.get_dict()
il.close()

form_data = {
    'authenticity_token': authenticity_token,
    'utf8': '',
    'login': 'kidellwq',
    'password': '857463sdc',
    'commit': 'Sign in',
}

i2 = requests.post('https://github.com/session', data=form_data, cookies=cl)
c2 = i2.cookies.get_dict()
cl.update(c2)
i3 = requests.get('https://github.com/settings/repositories', cookies=cl)

soup3 = BeautifulSoup(i3.text, features='html.parser')
list_group = soup3.find(name='div', class_='listgroup')

for child in list_group.children:
    if isinstance(child, Tag):
        project_tag = child.find(name='a', class_='mr-1')
        size_tag = child.find(name='small')
        temp = "项目:%s(%s).项目路径:%s" % (project_tag.get('href'), size_tag.string, project_tag.string,)
        print(temp)
