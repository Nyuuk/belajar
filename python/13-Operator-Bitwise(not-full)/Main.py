# episode operator biwise, operasi biner, binary
a = 9
b = 5

# bitwise OR(|)
c = a | b
print("\n",5*'=','OR',5*'=')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print(' ',10*'-','(|)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise AND(&)
c = a & b
print("\n",5*'=','AND',5*'=')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print(' ',10*'-','(&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise XOR(^)
c = a ^ b
print("\n",5*'=','XOR',5*'=')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print(' ',10*'-','(^)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise NOT(~)
c = ~a
print('nilai :',a,' , binary :',format(a,'08b'))
print(' ',10*'-','(~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print(' ',10*'-','(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))
