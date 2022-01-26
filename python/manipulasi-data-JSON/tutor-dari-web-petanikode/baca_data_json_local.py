# gunakan modul json
import json

#buka file json
file_json = open('dataku.json')

# parsing data JSON
data = json.loads(file_json.read())

# cetak isidata JSON
print(data)

# modifikasi print
print(f"\nNama: {data['nama']}")
print(f"Website: {data['web']}")
print(f"Sosial Media:")
print(f"- Facebook: {data['social_media']['facebook']}")
print(f"- Twitter: {data['social_media']['twitter']}")
print(f"- Facebook: {data['social_media']['instagram']}")
