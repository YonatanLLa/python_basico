# Typla -> Inmutable
alumnos = ('yonatan', 'juan', 'carlos', 'yonatan')

#count -> Contar la cantidad de valores
cantidad_yonatan = alumnos.count('yonatan')
print(cantidad_yonatan)

#Index -> Devuelve la posicion o el indice del valor a buscar

posicion_juan = alumnos.index('juan')
print(f'La posicion de juan es: {posicion_juan}')

##############
# Convertimos tupla a una lista (para añadir valores)
print(f'Tipo de Datos: {type(alumnos)}')
alumnos_listas = list(alumnos)
print(f'Tipo de Datos: {type(alumnos_listas)}')
alumnos_listas.append("Emily")

alumnos = tuple(alumnos_listas)
print(f'Tipo de Datos: {type(alumnos)}')

