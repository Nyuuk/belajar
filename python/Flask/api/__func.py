from os import path
import json
if not path.exists('data.json'):
    with open('data.json', 'w') as f:
        f.write(json.dumps(
            {"token-api": [{'name': 'example', 'token': 'like-you'}]},
            indent=2
            )
        )
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data
token = [dat['token'] for dat in get_data()['token-api']]
def auth(header):
    "header is request.headers"
    auth = header.get("X-Api-Key")
    for i in token:
        if str(i) == str(auth):
            return str(auth) == str(i)
def get_name_token(header):
    """
    header is request.headers
    akan mereturn nama dari token request
    """
    auth = header.get('X-Api-Key')
    for i in get_data()['token-api']:
        if i['token'] == str(auth):
            return i['name']
