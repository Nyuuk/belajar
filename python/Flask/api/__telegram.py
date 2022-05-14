import json
from .__func import get_data

if 'user-telegram' not in get_data():
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data['user-telegram'] = []
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()
user_id_data = [det['user_id'] for det in get_data()['user-telegram']]


def req_saldo(value):
    """
    fungsi untuk add/delete request modif saldo
    contoh value
    {"meth": "del/add", "user_id": 123, "saldo": 123}
    """
    from .__func import get_data
    user_id_data = [det['user_id'] for det in get_data()['user-telegram']]
    if 'request-saldo' not in get_data():
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data['request-saldo'] = []
            f.seek(0)
            json.dump(data, f, indent=2)
    if int(value['user_id']) not in user_id_data:
        return {"status": False, "message": "user belum terdaftar"}
    if value['meth'] == 'add':
        try:
            with open('data.json', 'r+') as f:
                data = json.load(f)
                for i in data['request-saldo']:
                    if str(value['user_id']) == str(i['user_id']) and str(value['saldo']) == str(i['saldo']):
                            return {"status": False, "message": "request sudah ada"}
                data['request-saldo'].append({"user_id": int(value['user_id']), "saldo": int(value['saldo'])})
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
        except Exception as ex:
            return {"status": False, "message": ex}
        else:
            return {"status": True, "message": "Success!!!"}
    elif value['meth'] == 'del':
        cd = [e for e in get_data()['request-saldo']]
        try:
            if not cd:
                return {"status": False, "message": "request kosong"}
            for i in range(len(cd)):
                if ((int(value['user_id']) == cd[i]['user_id']) and (int(value['saldo']) == cd[i]['saldo'])):
                    del cd[i]
                    status = True
                    break
                else:
                    status = False
        except Exception as ex:
            return {"status": False, "message": ex}
        else:
            if not status:
                return {"status": False, "message": "not found"}
            else:
                with open('data.json', 'r+') as f:
                    data = json.load(f)
                    data['request-saldo'] = cd
                    print(data['request-saldo'])
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
                return {"status": True, "message": "Success!!!"}
def new_user(value):
    """
    fungsi untuk menambakan user bot telegram
    contoh value
    {"user_id": 17271, "username": "username", "saldo": 0, "status": "user"}
    jika berhasil
    return {"status", "message": "Success!!!"}
    jika gagal
    return {"status": False, "message": ex}
    """
    value['akun'] = []
    user_id_data = [det['user_id'] for det in get_data()['user-telegram']]
    if int(value['user_id']) in user_id_data:
        print(value['user_id'] in user_id_data)
        return {"status": False, "message": "user sudah terdaftar"}
    else:
        try:
            with open('data.json', 'r+') as f:
                data = json.load(f)
                data['user-telegram'].append(value)
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
        except Exception as ex:
            return {"status": False, "message": ex}
        else:
            return {"status": True, "message": "Success!!!"}

def update_user(value):
    """
    fungsi untuk update user bot telegram
    contoh value
    {"user_id": 17271, "username": "username", "saldo": 0, "status": "user"}
    jika berhasil
    return {"status", "message": "Success!!!"}
    jika gagal
    return {"status": False, "message": ex}
    """
    user_id_data = [det['user_id'] for det in get_data()['user-telegram']]
    if int(value['user_id']) not in user_id_data:
        return {"status": False, "message": "user belum terdaftar"}
    try:
        with open('data.json', 'r+') as f:
            data = json.load(f)
            for i in range(len(data['user-telegram'])):
                if int(value['user_id']) == int(data['user-telegram'][i]['user_id']):
                    data['user-telegram'][i]['username'] = value['username']
                    status = True
                    break
                else:
                    status = False
            if status:
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
    except Exception as ex:
        return {"status": False, "message": ex}
    else:
        if status:
            return {"status": True, "message": "Success!!!"}
        else:
            return {"status": False, "message": "not found"}

def mod_saldo(user_id, saldo_new):
    """
    fungsi untuk mengubah saldo berdasarkan user_id
    user_id & saldo_new harus digit
    """
    user_id_data = [det['user_id'] for det in get_data()['user-telegram']]
    if int(user_id) not in user_id_data:
        return {"status": False, "message": "user belum terdaftar"}
    try:
        with open('data.json', 'r+') as f:
            data = json.load(f)
            for i in range(len(data['user-telegram'])):
                if int(user_id) == int(data['user-telegram'][i]['user_id']):
                    data['user-telegram'][i]['saldo'] = int(saldo_new)
                    status = True
                    break
                else:
                    status = False
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    except Exception as ex:
        return {"status": False, "message": ex}
    else:
        if status:
            return {"status": True, "message": "Success!!!"}
        else:
            return {"status": False, "message": "not found"}

def get_user(meth, user_id=None):
    """
    fungsi untuk mereturn user id, username, saldo, dan status
    meth mempunyai 2 obj yaitu ALL & USS
    ALL akan mereturn semua user bot
    user_id harus berupa digit
    jika berhasil USS
    return {"status": True, "message": {"user_id": 17271, "username": "username", "saldo": 0, "status": "user"}}
    """
    from .__func import get_data
    if str(meth) == 'USS':
        for i in get_data()['user-telegram']:
            if int(i['user_id']) == int(user_id):
                status = True
                break
            else:
                status = False
        if status:
            return {"status": True, "message": i}
        else:
            return {"status": False, "message": "not found"}
    elif str(meth) == 'ALL':
        return {"status": True, "message": get_data()['user-telegram']}

def get_req_saldo(meth, user_id=None):
    "fungsi untuk return list request saldo"
    user_id_data = [det['user_id'] for det in get_data()['user-telegram']]
    with open("data.json", 'r') as f:
        data = json.load(f)
    if meth == 'USS':
        if user_id == None:
            return {"status": False, "message": "user_id not defined"}
        if int(user_id) not in user_id_data:
            return {"status": False, "message": "user belum terdaftar"}
        for i in data['request-saldo']:
            if int(user_id) == int(i['user_id']):
                status = True
                break
            else:
                status = False
        if status:
            return {"status": True, "message": i}
        else:
            return {"status": True, "message": "not found"}
    elif meth == 'ALL':
        return {"status": True, "message": data['request-saldo']}
