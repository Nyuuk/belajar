import json
from urllib import request

url = 'https://jsonplaceholder.typicode.com/posts'

# lakukan http request
response = request.urlopen(url)

# parsing data
data = json.loads(response.read())

# gunakan perulangan untuk menampilkan data
#for i in range(len(data)):
#    print(f'{i}. {data[i]["title"]}')
for post in data:
    print(f"- {post['title']}")
