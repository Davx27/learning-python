number1 = 9
number2 = 5
result = number1 + number2
print(result)

print('----------------------')

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for item in tupla:
    if item != 3:
        print(item)
        
contador = 0 
while tupla[contador] == 12:
    print(tupla[contador])
    contador += 1 

while True:
    for numero in tupla:
        if numero == 1:
            print(numero)
            activo = False


            