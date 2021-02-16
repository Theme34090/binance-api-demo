import requests

URI = 'https://notify-api.line.me/api/notify'


def notify(auth_token, data):
    headers = {'Authorization': 'Bearer ' + auth_token}
    r = requests.post(URI, data=data, headers=headers)
    print(r.status_code)
