import requests

post_dict = {
    'phone': '8615939949937',
    'password': '123456',
    'oneMonth': 1,
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.335'
                  '9.181 Safari/537.36',
}
res1 = requests.get(
    url="https://dig.chouti.com/",
    headers=header,
)
cookies_dict1 = res1.cookies.get_dict()
res2 = requests.post(
    url="https://dig.chouti.com/login",
    data=post_dict,
    headers=header,
    cookies=cookies_dict1,
)
cookies_dict2 = res2.cookies.get_dict()
res3 = requests.get(
    url="https://dig.chouti.com/profile",
    headers=header,
    cookies={'gpsd': cookies_dict1['gpsd']}
)

cookies_dict3 = res3.cookies.get_dict()
print(cookies_dict1)
print(cookies_dict2)
print(res3.text)
