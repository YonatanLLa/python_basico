inicio = ['Arnold', 'Alfredo', 'anthony']
print(f"Inicio: {inicio}")

# Agregar un valor
inicio.append('Freddy')
print(f'append: {inicio}')

# Agregar un valor en una posicion especifica
inicio.insert(1, 'yonatan')
print(f'insert: {inicio}')

# Extender la lista
inicio_dos = ['python', 'javascript']
inicio.extend(inicio_dos)
print(f'extend: {inicio}')

# Ver la posicion de tu lista
posicion_python = inicio.index("python")
print(f'La posicion del indice de python es: {posicion_python}')

# Removerla lista, la primera que encuetra
inicio.remove('yonatan')
print(f'Removemos a yonatan: {inicio}')

# Remover por posicion o indice
inicio.pop(1)
print(f'Removemos de la posicion 1 Arnold: {inicio}')

# count -> retorna las veces que existe el mismo valor
muchas_veces = inicio.count("yonatan")
print(f'muchas veces: {muchas_veces}')

# cantidad de valores de la lista 
print(f'Cantidad de veces: {len(inicio)}')