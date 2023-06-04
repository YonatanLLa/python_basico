#Try Except
# Manejo de errores.
# Controlando el error de diferentes casos.
try:
    dividendo = int(input("Ingresa el dividento: "))
    divicion = 5/dividendo
    print(divicion)
except (TypeError, ValueError):
    print('El valor de dividendo no se esta formateando a numero')
except ZeroDivisionError:
    print('Ocurrio un error, porque se esta dividiendo con 0')
# ver que tipo de error se esta generando ->
# catura todo lo que esta arriba, la clase especifica por que es el error
except Exception as e: #alias
    print(e.__class__)
    
