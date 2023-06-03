meses = ['Enero', 'Febreor', 'Marzo', 'Abril']
'''
print(list(enumerate(meses)))'''
# Obtener el valor
for mes in meses:
    print(mes)


for mes in meses:
    if mes == 'Enero':
        print(mes)

## Obtener el indice y el valor
# enumerate -> (index, value) <- tuplas [(0,'Enero'),(1, 'Febrero')]
for index, mes in enumerate(meses):
    print(index, mes)

# range -> recibe 3 argumentos (parametros)
# 1° Desde donde empieza
# 3° hata donde finaliza
# 2° De cuanto en cunato incrementara
# numero = [0,1,2,3,4,5]

for numero in range(6,0,-1):
    print(f'Range: {numero}')


persona = {
    "nombres":"Yonatan Llanto",
    "edad":20,
    "hobbies": ["Futbol", "Nadar", "Jugar"]
}

# 1.- Forma de obtener keys
for index in persona:
    print(index, persona[index])

# 2.- Obtener keys
for index in persona.keys():
    print(index)

# 1.- Obtener value
for value in persona.values():
    print(value)

# Obtener la keys and values.
for key, value in persona.items():
    print(key, value)