# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean
# >, <, >=, <=, !=, ==, is, is not

a = 4
b = 2

# lebih besar dari >
print('========== lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print('========== kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan (>=)
print('========== lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan (<=)
print('========== kurang dari sama dengan (<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

#  sama dengan (==)
print('==========  sama dengan (==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a == 2
print(a,'==',2,'=',hasil)

# tidak sama dengan (!=)
print('========== tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = a != 2
print(a,'!=',2,'=',hasil)


# 'is' sebagai komparasi object identity
print('========== object identity (is)')
x = 5 # ini adalah assigment membuat object
y = 5
print('Nilai x =',x,', id =',hex(id(x)))
print('Nilai y =',y,', id =',hex(id(y)))
hasil = y is x
print('y is x =',hasil)

# 'is' sebagai komparasi object identity
print('========== object identity (is)')
x = 5 # ini adalah assigment membuat object
y = 3
print('Nilai x =',x,', id =',hex(id(x)))
print('Nilai y =',y,', id =',hex(id(y)))
hasil = y is x
print('y is x =',hasil)

# 'is not not' sebagai komparasi object identity
print('========== object identity (is not not)')
x = 5 # ini adalah assigment membuat object
y = 5
print('Nilai x =',x,', id =',hex(id(x)))
print('Nilai y =',y,', id =',hex(id(y)))
hasil = y is not x
print('y is not x =',hasil)

# 'is not' sebagai komparasi object identity
print('========== object identity (is not)')
x = 5 # ini adalah assigment membuat object
y = 3
print('Nilai x =',x,', id =',hex(id(x)))
print('Nilai y =',y,', id =',hex(id(y)))
hasil = y is not x
print('y is not x =',hasil)



