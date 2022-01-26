import json
from urllib import request

url = 'https://api.kawalcorona.com/'

response = request.urlopen(url)

data = json.loads(response.read())

for i in range(len(data)):
    print(f"- Country  : {data[i]['attributes']['Country_Region']}")
    print(f"  Positif  : {data[i]['attributes']['Confirmed']}")
    print(f"  Sembuh   : {data[i]['attributes']['Recovered']}")
    print(f"  Meninggal: {data[i]['attributes']['Deaths']}")
