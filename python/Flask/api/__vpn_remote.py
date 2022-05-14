import json
from .__func import get_data
import pytz
import datetime as dt

dat = get_data()
status = False
if 'user-telegram' not in dat:
    dat['user-telegram'] = []
    status = True
if 'layanan' not in dat:
    dat['layanan'] = {"vpnremote": []}
    status = True
else:
    if 'vpnremote' not in dat['layanan']:
        dat['layanan'] = {"vpnremote": []}
        status = True
if status:
    with open('data.json', 'r+') as f:
        f.seek(0)
        json.dump(dat, f, indent=2)
        f.truncate()

tz = pytz.timezone('Asia/Jakarta')

def get_last_ip():
    "Fungsi untuk generate last ip"
    from .__func import get_data
    last_ip = 2
    for i in get_data()['layanan']['vpnremote']:
        if i['iplocal'].split('.')[3] == last_ip:
            last_ip += 1
    return last_ip

def add_uss(value):
    """
    append new user vpn remote
    value:
    {'created_by': ['user-telegram/user-web-dll', id_user], 'perpanjang': True/False, 'uss_vpn': 'uss_vpn', 'pw_vpn': 'pw_vpn', 'fwd_1': portlocal, 'fwd_2': portlocal, 'fwd_3': portlocal, 'exp': 'YYYY-MM-DD H:M'}
    """
    from .__func import get_data
    uss_vpn_data = [a['uss_vpn'] for a in get_data()['layanan']['vpnremote']]
    for i in uss_vpn_data:
        if str(value['uss_vpn']) == str(i):
            return {"status": False, "message": "user sudah ada, mohon ganti user anda"}
    try:
        dt.datetime.strptime("%s" % (value['exp']), '%Y-%m-%d %H:%M')
    except:
        return {"status": False, "message": "format expired salah"}
    for i in value:
        if 'fwd' in i:
            if isinstance(value[i], int):
                value[i] = value[i]
            elif value[i].isdigit():
                value[i] = int(value[i])
            elif value[i].lower() == 'winbox':
                value[i] = 8291
            elif value[i].lower() == 'api':
                value[i] = 8728
            elif value[i].lower() == 'api-ssl':
                value[i] = 8729
            elif value[i].lower() == 'web':
                value[i] = 80
            elif value[i].lower() == 'ftp':
                value[i] = 21
            elif value[i].lower() == 'telnet':
                value[i] = 23
            elif value[i].lower() == 'ssh':
                value[i] = 22
            else:
                return {"status": False, "message": "format %s harus berupa digit/nomor" % (i)}
    value['iplocal'] = '10.10.0.%s' % (get_last_ip())
    value['crated_in'] = str(dt.datetime.now(tz).strftime('%Y-%m-%d %H:%M'))
    #import delegator
    #add_akn = delegator.run('useradd -s /bin/false -M %s' %s (value['uss_vpn']))
    #if add_akn.return_code == 9:
        #return {"status": False, "message": "user sudah ada"}
    #add_pw = delegator.run(r'echo "%s\n%s\n"|passwd %s' % (value['pw_vpn'], value['pw_vpn'], value['uss_vpn']))
    try:
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data['layanan']['vpnremote'].append(value)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    except Exception as ex:
        return {"status": False, "message": ex}
    else:
        return {"status": True, "message": value}

def del_uss(value):
    """
    delete user vpn remote
    value:
    {'uss_vpn': 'uss_vpn'}
    """
    from .__func import get_data
    get_dit = get_data()['layanan']['vpnremote']
    if not bool(get_dit):
        return {"status": False, "message": "not found user vpnremote"}
    for i in range(len(get_dit)):
        if get_dit[i]['uss_vpn'] == value['uss_vpn']:
            del get_dit[i]
            status = True
            break
        else:
            status = False
    if status:
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data['layanan']['vpnremote'] = get_dit
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
            return {"status": True, "message": "Success!!!"}
    else:
        return {"status": False, "message": "user not found"}

def mod_uss(value):
    """
    modif user vpnremote
    value:
    {'created_by': ['user-telegram/user-web-dll', id_user](optional), 'perpanjang': True/False(optional), 'uss_vpn': 'uss_vpn', 'pw_vpn': 'pw_vpn'(optional), 'fwd_1': portlocal(optional), 'fwd_2': portlocal(optional), 'fwd_3': portlocal(optional), 'exp': 'YYYY-MM-DD H:M'(optional)}
    value semua optional, kecuali uss_vpn
    """
    data = get_data()['layanan']['vpnremote']
    js = {'created_by': False, 'perpanjang': False, 'uss_vpn': False, 'pw_vpn': False, 'exp': False}
    for n in range(len(data)):
        if data[n]['uss_vpn'] == value['uss_vpn']:
            if 'created_by' in value:
                if len(value['created_by']) == 1:
                    data[n]['created_by'] == value['created_by']
                    js['created_by'] = True
            if 'perpanjang' in value:
                if (value['perpanjang'] == True) or (value['perpanjang'] == False):
                    data[n]['perpanjang'] = value['perpanjang']
                    js['perpanjang'] = True
            if 'pw_vpn' in value:
                data[n]['pw_vpn'] = value['pw_vpn']
                #import delegator
                #mod_pw = delegator.run(
                    #r'echo "%s\n%s\n"|passwd %s' % (
                        #value['pw_vpn'], value['pw_vpn'], value['uss_vpn']
                        #)
                    #)
                data[n]['pw_vpn'] = value['pw_vpn']
                js['pw_vpn'] = True
            if 'exp' in value:
                try:
                    dt.datetime.strptime("%s" % (value['exp']), '%Y-%m-%d %H:%M')
                except:
                    return {"status": False, "message": "format expired salah"}
                else:
                    data[n]['exp'] = value['exp']
                    js['exp'] = True
            for i in value:
                if 'fwd' in i:
                    if i in data[n]:
                        data[n][i] = value[i]
                        js[i] = True
    dt = ""
    for i in js:
        if js[i]:
            dt += "%s modifed " % (i)
    if bool(dt):
        try:
            with open('data.json', 'r+') as f:
                det = json.load(f)
                det['layanan']['vpnremote'] = data
                f.seek(0)
                json.dump(det, f, indent=2)
                f.truncate()
        except Exception as ex:
            return {"status": False, "message": ex}
        return {"status": True, "message": "Success!!! %s" % (dt)}
    else:
        return {"status": False, "message": "not found value"}
