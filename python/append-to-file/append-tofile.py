#with open('test.txt', 'a') as f:
#    f.write('Hello')

with open('test.txt', 'r+') as fa:
    fa.seek(3)
    fa.write(' | append with r+ |')
