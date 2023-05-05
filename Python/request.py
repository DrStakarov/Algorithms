import requests

req = requests.get('https://www.google.com')
print(req.url)
print(req.status_code)