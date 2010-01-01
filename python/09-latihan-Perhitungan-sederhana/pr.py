# Fahrenheit to kelvin
fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
kelvin = (5/9 * ( fahrenheit - 32 )) + 273
print('Suhu Fahrenheit adalah', fahrenheit)
print('Suhu dalam kelvin adalah', kelvin)

# Kelvin to Fahrenheit
kelvin = float(input('Masukan suhu dalam kelvin : '))
fahrenheit = 9/5 * (kelvin - 273) + 32
print('Suhu kelvin adalah', kelvin)
print('Suhu dalam fahrenheit adalah', fahrenheit)
