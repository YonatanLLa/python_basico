# Ejercicio 3: Calcular el factorial de un número.
'''
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2 * 1
4! = 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1
'''

numero = int(input("Ingrese el numero: "))

fatorial = 1
if numero == 0:
    fatorial *= 0
elif numero > 0:
    for num in range(1, numero + 1, 1):
        fatorial *= num
else:
    print('Numero no puede ser negativo')

print(fatorial)
