import json
from urllib import request

# tentukan url endpoint
url = 'https://api.github.com/users/nyuuk'

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# cetak hasil parsing json
print("== Program Baca Profile Github ==")
print(f"Nama: {data['name']}")
print(f"Lokasi: {data['location']}")
print(f"Institusi: {data['company']}")
print(f"Folower: {data['followers']}")
print(f"mendaftar github pada: {data['created_at']}")
