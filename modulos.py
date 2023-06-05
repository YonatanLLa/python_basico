# instalar dependecia o librerias

# !incorrecta
# from operadores import variables
# nombre = variables.nombre
# print(nombre)

# as -> es un alias.
from operadores.variables import nombre, last_name
from camelcase import CamelCase as ClaseCamel

instancia = ClaseCamel()  # Agrega paréntesis aquí
texto = 'Soy el mejor'

print(instancia.hump(texto))
print(nombre, last_name)
