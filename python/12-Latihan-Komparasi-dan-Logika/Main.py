# latihan logika dan komparasi
# membuat gabungan area rentang dari angka


# ++++3------10++++++
inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n== "))

# ++++++3-----------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

# ---------10+++++++
# memeriksa angka lebih dari
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan :', isCorrect)


# -----3+++++++10-----
print("\n",12*"=","\n")
inputUser = float(input("Masukan angka yang bernilai\nlebih dari 3\natau\nlebih kecil dari 10\n== "))

# ------------3++++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =",isLebihDari)
# +++++++++++10------
# Kurang dari 10
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =",isKurangDari)

# -----3+++++++10-----
isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukan :', isCorrect)
