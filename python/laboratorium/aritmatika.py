from time import sleep
a = 4756121
jumlah = []

while a > 0:
    if a >= 100000:
        jumlah.append(100000)
        a -= 100000
    else:
        jumlah.append(a)
        a -= a
to = 0
for i in range(len(jumlah)):
    if i == 0:
        na = jumlah[i]
    else:
        na += jumlah[i]
    for num in range(to, na):
        sleep(0.001)
        print(num, ' | ')
    to += jumlah[i]
    print('pergantian')
    sleep(1)
