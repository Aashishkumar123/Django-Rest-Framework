import requests

url = 'http://127.0.0.1:8000/Api/delete/2'

r = requests.delete(url=url)
print(r.content)
