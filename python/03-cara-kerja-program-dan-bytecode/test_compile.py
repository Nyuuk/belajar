import time
start_time = time.time()

print("Hello")
print("World") # akan mengeprint per baris
print("Hello World!!!")

# baris kosong akan di lewati
# ini adalah comment
"""
ini koment multiline
"""
a = 10 # ini adalah assigment
# asigment harus sebelum pemanggil
print(a)
for i in range(1,1000):
    a = 10

print(time.time() - start_time, "detik")
"""
source code = syntax
contoh source code adalah command di atas
kita bisa mengcompile python ke yang namanya bytecode
cara mengcompile python 
$ python -m py_compile Main.py
setelah selesai akan membuat folder baru bernama __pycache__
yang isi nya adlah hasil compile an
"""
