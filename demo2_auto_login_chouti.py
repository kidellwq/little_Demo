import requests

post_diict = {
	'phone': 15939949937,
	'password': 111111,
	'oneMonth': 1,
}
response = requests.post(
	url = "https://dig.chouti.com/login",
	data = post_diict
)

print(response.text)