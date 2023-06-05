#Funcion en python: se utiliza como camelcase.

def nameFunction():
    pass #Logica

# Function in the action
def saludar(nombre):
    print(type(nombre))
    print(f'Hi {nombre}, haw are you?')

saludar('yonatan')

# Funtion -> Todos los que tienen parametros por defecto tienen que ir al final
def saludarSegundo(apellidos,nombre="Yonatan"):
    print(f'hi {nombre} {apellidos}')

saludarSegundo(nombre='Pedro', apellidos='Rocca')

# Funciones con multiparametros
# *args -> nos ayuda a recibir valores infinitos como argumentos
# Retornara o se obtendra una tubla con todos los valores
# ejem: nombreFuntion("Value1", "Value2", .... , "ValueX")

def alumnosInscritos(*args):
    for arg in args:
        print(arg)
        
alumnosInscritos("a","c","d","e","y","p")

# **kwargs -> nombreFunction(valor_uno = 1, valor_dos = 2, ... valor_X = X)

def cursosAlumnos(**kwargs):
    print(kwargs)
cursosAlumnos(a = "algebra", b = "geometria")