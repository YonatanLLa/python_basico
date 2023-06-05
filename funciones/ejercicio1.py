# Ejercicio 1
# crear una funcion que reciba dos numeros donde el primer numero tenga un valor: 10 por defecto, si la suma de dicho numero es par.
# -> mostrar la mitad de la suma
# -> si no lo es, mostrar la suma

def sumar(numero2, numero1=10):
    suma_total = numero1 + numero2
    print(int(suma_total/2)) if suma_total % 2 == 0 else print(suma_total)


sumar(numero2=1)
