# 2 PR
# ---0+++5---8+++11---
# +++0---5+++8---11+++

# ---0+++5---8+++11---
print("\n",5*'-','0',5*'+','5',5*'-','8',5*'+','11',5*'-',"\n")
inputUser = float(input("Masukan angka\nlebih dari 0, kurang dari 5, lebih dari 8, kurang dari 11\n?? "))
i0 = (inputUser > 0)
i8 = (inputUser > 8)
i5 = (inputUser < 5)
i11 = (inputUser < 11)
hasil1 = (i0 and i5)
hasil2 = (i8 and i11)
isCorrect = (hasil1 or hasil2)
print('Hasil 0+++5  =',hasil1)
print('Hasil 8+++11 =',hasil2)
print('Hasil ---0+++5---8+++11--- =',isCorrect)


# +++0---5+++8---11+++
print("\n",5*'+','0',5*'-','5',5*'+','8',5*'-','11',5*'+',"\n")
inputUser = float(input("Masukan angka\nkurang dari 0, lebih dari 5, kurang dari 8, kurang dari 11\n?? "))
i0 = (inputUser < 0)
i8 = (inputUser < 8)
i5 = (inputUser > 5)
i11 = (inputUser > 11)
isCorrect = ((i0 or i11) or (i5 and i8) )
print(inputUser,'< 0  =',i0)
print(inputUser,'< 8  =',i8)
print(inputUser,'> 5  =',i5)
print(inputUser,'> 11 =',i11)
print('Hasil +++0---5+++8---11+++ =',isCorrect)
