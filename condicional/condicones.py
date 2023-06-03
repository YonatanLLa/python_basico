## IF -ELSE
# palabra reservada pass, le decimonos aqui voy agregar algo mas tarde
'''numero = 10

if numero == 10:
    pass
else:
    pass'''

edad = int(input("Ingrese tu edad: "))

if edad > 18:
    print('Eres mayor de edad')
elif edad == 18: 
    print('Tienes 18 años')
else:
    print("Eres menor de edad")

# Operador Ternario

ternario = 'Ternario: '+'Eres mayor de edad' if edad >=18 else'Ternario: '+ 'Eres menor de edad'

print(ternario)