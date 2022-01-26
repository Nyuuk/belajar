import json
import os
"""
[
  {
  "user": "adnan",
  "password": "test",
  "namadep": "Adnan",
  "namabel": "Khafabi",
  "lokasi": "Cikarang Utara",
  "umur": "18"
  }
]
"""

path = './json/'
user_js = 'user.json'

if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path + user_js):
    os.mknod(path + user_js)

def write_js(namdep, nambel, lok, umur):
    with open(path + user_js, 'r+') as asli_r:
        data = json.load(asli_r)
        json_string = {"namadep": "%s"%namdep, "namabel": "%s"%nambel, "umur": "%s"%umur, "lokasi": "%s"%lok}
        data.append(json_string)
        asli_r.seek(0)
        json.dump(data, asli_r, indent=2)
        asli_r.truncate

print('\n== Program manipulasi JSON ==')
print('1. Baca file json')
print('2. Tulis file json')
print('3. Ganti file json')
print('4. Delete file json')
a = input('Input number? ')
if a.isdigit() == True:
    if a == '1':
        with open(path + user_js) as js_file:
            data = json.loads(js_file.read())
            for i in range(len(data)):
                print(f"- Name     : {data[i]['namadep']} {data[i]['namabel']}")
                print(f"  Age      : {data[i]['umur']}")
                print(f"  Location : {data[i]['lokasi']}")
    elif a == '2':
        namdep = input('Input nama depan ? ')
        nambel = input('Input nama belakang ? ')
        lok = input('Input lokasi ? ')
        umur = input('Input Umur ? ')
        write_js(namdep, nambel, lok, umur)
    elif a == '3':
        with open(path + user_js, 'r+') as js:
            data = json.load(js)
            for i in range(len(data)):
                print(f"{i}. - Name     : {data[i]['namadep']} {data[i]['namabel']}")
                print(f"     Age      : {data[i]['umur']}")
                print(f"     Location : {data[i]['lokasi']}")
                total = i
            number = int(input("Pilih berdasarkan nomor, nomor berapa ? "))
            if number <= total:
                namdep = input('Input nama depan ? ')
                nambel = input('Input nama belakang ? ')
                umur = input('Input Umur ? ')
                lok = input('Input lokasi ? ')
                if(len(namdep)):
                    data[number]['namadep'] = namdep
                if(len(nambel)):
                    data[number]['namabel'] = nambel
                if(len(lok)):
                    data[number]['lokasi'] = lok
                if(len(umur)):
                    data[number]['umur'] = umur
                js.seek(0)
                json.dump(data, js, indent=4)
                js.truncate()
                print('Berhasil !!!')
            else:
                print('nomor salah')
    elif a == '4':
        with open(path + user_js, 'r+') as js:
            data = json.load(js)
            for i in range(len(data)):
                print(f"{i}. - Name     : {data[i]['namadep']} {data[i]['namabel']}")
                print(f"     Age      : {data[i]['umur']}")
                print(f"     Location : {data[i]['lokasi']}")
                total = i
            number = int(input("Pilih berdasarkan nomor, nomor berapa yang akan di hapus? "))
            if number <= total:
                del data[number]
                js.seek(0)
                json.dump(data, js, indent=4)
                js.truncate()

