import json
from .__func import get_data
import pytz
import datetime as dt

class Xray:
    """
    class untuk layanan xray
    """
    def __init__(self):
        self.users = get_data()['layanan']['xray']
        if 'servers' not in get_data():
            with open('data.json', 'r+') as f:
                data = json.load(f)
                f.seek(0)
                data['servers'] = []
                json.dump(data, f, indent=2)
                f.truncate()
        self.servers = get_data()['servers']
    def push_to_users_data(self, value):
        """
        value is data users in layanan > xray
        """
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data['layanan']['xray'] = value
            f.seek(0)
            json.dump(value, f, indent=2)
            f.truncate()
    def modif_user_data(self, value):
        """
        value:
        {"metode": "new or edit"}
        jika metode new, maka value wajib adalah:
        {"metode": "new", "created_by":
        ["user-telegram/user-web/dll", "123"],
        "username": "uss", "exp": "YYYY-MM-DD H:m", "server": "biznet-jakarta/biznet-banten"}
        jika metode edit, maka value wajib adalah username yang lain optional

        """
        js = []
        data = self.users
        ls_val = [det for det in value]
        if 'username' not in ls_val:
            return {"status": False, "message": "username not defined"}
        for i in range(len(data)):
            if data[i]['username'] == value['username']:
                username = True
                break
            else:
                username = False
        if username:
            # metode edit if username True
            if value['metode'] == 'edit':
                    for det in ls_val:
                        if 'uuid' in det:
                            if len(value[det]) == 36:
                                data[i]['uuid'] = value[det]
                                js.append(det)
                        if 'username' in det:
                            data[i]['username'] = value[det]
                            js.append(det)
                        if 'created_by' in det:
                            if len(value[det]) == 2:
                                data[i]['created_by'] = value[det]
                                js.append(det)
                        if 'exp' in det:
                            try:
                                dt.datetime.strptime("%s" % (value[det]), "%Y-%m-%d %H:%M")
                            except:
                                return {"status": False, "message": "format expired salah"}
                            else:
                                data[i]['exp'] = value[det]
                                js.append(det)
                        if 'server' in det:
                            if value[det] not in self.servers:
                                return {"status": False, "message": "%s not in list servers" % (value[det])}
                            data[i]['server'] = value[det]
                            js.append(det)
                    if bool(js):
                        dt = ""
                        for i in range(len(js)):
                            if i == len(js):
                                dt += "%s modified" % (js[i])
                            else:
                                dt += "%s modified, " % (js[i])
                        return {"status": True, "message": "Success!!! %s" % (dt)}
                    else:
                        return {"status": False, "message": "not modified"}
                    # push to data.json
                    self.push_to_users_data(data)
            # metode delete if username True
            elif value['metode'] == 'delete':
                del data[i]
                # push to data.json
                self.push_to_users_data(data)
                return {"status": True, "message": "Success!!!"}
            # metode new if username True
            elif value['metode'] == 'new':
                return {"status": False, "message": "username sudah ada"}
            else:
                return {"status": False, "message": "metode is wrong"}
        # else username
        else:
            # metode new
            if value['metode'] == 'new':
                if 'username' not in ls_val:
                    return {"status": False, "message": "username not defined"}
                if 'server' not in ls_val:
                    return {"status": False, "message": "server not defined"}
                if 'exp' not in ls_val:
                    return {"status": False, "message": "exp not defined"}
                if 'created_by' not in ls_val:
                    return {"status": False, "message": "created_by not defined"}
                else:
                    if len(value['created_by']) != 2:
                        return {"status": False, "message": "created_by has a 2 list. one is string and two is int"}
                data.append(value)
                # push to data.json
                self.push_to_users_data(data)
            elif value['metode'] == 'new' or value['metode'] == 'delete':
                return {"status": False, "message": "username not found"}

