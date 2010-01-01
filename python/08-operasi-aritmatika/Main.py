# Operasi aritmatika

a = 10
b = 3

# Operasi tambah + 
hasil = a + b
print(a,'+',b,'=',hasil,'(Pertambahan)')

# Operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil,'(Pengurangan)')

# Operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil,'(Perkalian)')

# Operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil,'(Pembagian)')

# Operasi exponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil,'(Exponen)')

# Operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil,'(Modulus)')

# Operasi floor division // 
hasil = a // b
print(a,'//',b,'=',hasil,'(Floor Division)')


# Prioritas operasi, operational precedence
"""
1. ()
2. exponen **
3. perkalian dan teman2 * / ** % //
4. pertambahan & pengurangan + -
"""
x = 3 
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
# 3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# Kurung '()' akan mengambil langkan paling pertama
hasil = ( x + y ) * z
print('(',x,'+',y,') *',z,'=',hasil)

















