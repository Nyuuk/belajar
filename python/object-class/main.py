import json
import os
users_js = 'user.json'
if not os.path.exists(users_js):
    with open(users_js, 'w') as f:
        f.write('''[
    {
        "user_id": "5270595605",
        "username": "None",
        "first_name": "Dnan",
        "last_name": "0794",
        "status": "user"
    },
    {
        "user_id": "647974546",
        "username": "elbaricho",
        "first_name": "Elba",
        "last_name": "None",
        "status": "user"
    }

]''')
ids = '723612441'
user = 'Nyuuk2'
first = 'Nyuuk'
last = 'None'

class upDate:
    def update_uss(self, chat_id, chat_username, chat_first, chat_last):
        self.id = chat_id
        self.uss = chat_username
        self.first = chat_first
        self.last = chat_last
        dict = {
    "id": "%s"%self.id,
    "uss": "%s"%self.uss,
    "first": "%s"%self.first,
    "last": "%s"%last
}
        with open(users_js, 'r+') as f:
            data = json.load(f)
            data_r = f.read()
            print(dict['id'])
            if str(dict['id']) not in data_r:
                json_ex = {"user_id": "%s"%self.id, "username": "%s"%self.uss, "first_name": "%s"%self.first, "last_name": "%s"%chat_last, "status": "user"}
                data.append(json_ex)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate
            else:
                for i in range(len(data)):
                    print(self.id, self.uss, self.first, self.last)
                    if dict['id'] in data[i]['user_id']:
                        if str(self.uss) not in data[i]['username']:
                            data[i]['username'] = str(self.uss)
                        if str(self.first) not in data[i]['first_name']:
                            data[i]['first_name'] = str(self.first)
                        if str(self.last) not in data[i]['last_name']:
                            data[i]['first_name'] = str(self.last)
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate
                        continue

objs = upDate()
objs.update_uss(ids, user, first, last)
