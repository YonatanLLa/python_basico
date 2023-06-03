# Ejercicio 2: Calcular el máximo de tres números:

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if numero1 > numero2:
    print(f"primer numero  es mayor: {numero1} N1")
elif numero2 > numero1:
    print(f"numero2 es mayor: {numero2} N2")
elif numero3 > numero2:
    print(f"numero3 es mayor: {numero3} N3")
