import requests

URL = 'http://127.0.0.1:8000/postDATA'
DATA = {
    'username': 'admin',
    'password': 'P@SSW)RD',
    'action': 'doLOGIN'
}

req = requests.post(url = URL, data = DATA)
print(req.status_code)
print(req.text)