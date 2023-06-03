# Ejercicio 1: Determinar si un número es primo.

num_primo = int(input("Ingresa el numero a determinar: "))

if num_primo>1:
    es_primo = True

    for i in range(2, num_primo):
        if num_primo % i == 0:
            es_primo = False
            break
    if es_primo:
        print('El numero es primo')
    else:
        print('El numero no es primo')
else:
    print("El numero no es primo")