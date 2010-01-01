
# operasi logika atau boolena
# not, or, and, xor

# Not
print('====NOT====')
a = True
c = not a
print('data a =',a)
print('--------- NOT')
print('data c =',c)

# OR (Jika terdapat True, maka hasil nya akan true)
print('====OR====')
a = True
b = True
hasil = a or b
print(a,' OR',b,' =',hasil)
a = False
b = False
hasil = a or b
print(a,'OR',b,'=',hasil)
a = True
b = False
hasil = a or b
print(a,' OR',b,'=',hasil)
a = False
b = True
hasil = a or b
print(a,'OR',b,' =',hasil)


# AND (jika 2 buah nilai True, maka hasilnya True)
print('====AND====')
a = True
b = True
hasil = a and b
print(a,' AND',b,' =',hasil)
a = False
b = False
hasil = a and b
print(a,'AND',b,'=',hasil)
a = True
b = False
hasil = a and b
print(a,' AND',b,'=',hasil)
a = False
b = True
hasil = a and b
print(a,'AND',b,' =',hasil)

# XOR (akan true, jika salah satunya true, sisanya false)
print('====XOR====')
a = True
b = True
hasil = a ^ b
print(a,' XOR',b,' =',hasil)
a = False
b = False
hasil = a ^ b
print(a,'XOR',b,'=',hasil)
a = True
b = False
hasil = a ^ b
print(a,' XOR',b,'=',hasil)
a = False
b = True
hasil = a ^ b
print(a,'XOR',b,' =',hasil)

