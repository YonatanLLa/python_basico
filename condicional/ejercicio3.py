# Ejercicio 3: Verificar si un año es bisiesto:
año = input("ingrese el año: ")


if año % 4 == 0 and (año%100 != 0 or año%400 ==0):
    print(f"El año: {año} es bisiesto")
else:
    print("El año no es bisiesto")