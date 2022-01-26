import json

#with open('t.json', 'r+') as f:
#    data = json.load(f)
#    data = {"name": "adnan"} # <--- add `id` value.
#    f.seek(0)        # <--- should reset file position to the beginning.
#    print(data)
#    json.dump(data, f, indent=4)
#    f.truncate()     # remove remaining part
json_string = {
        "nama": "test",
        "umur": "17",
        "tinggal": "cik"
}
with open('user.json', 'r+') as f:
    data = json.load(f)
    data.append(json_string)
    print(data)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
