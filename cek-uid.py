def get_uid_in_exp():
    with open('exp', 'r') as exp_f:
        uid_exp = exp_f.read()
    uuid = []
    for i in uid_exp.splitlines():
        if i.split()[1] == "NEVER":
            uuid.append(i.split()[2])
        else:
            uuid.append(i.split()[3])
    return uuid

with open('acc', 'r') as f_file:
    data = f_file.read()
data = data.replace(',', '').replace('"', '').splitlines()

for i in range(len(data)):
    for r in get_uid_in_exp():
        if data[i] == r:
            print(data[i])
        else:
            continue
