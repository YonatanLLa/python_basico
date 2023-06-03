# Diccionario -> (key => value)

persona = {
    "nombres":"Yonatan Llanto",
    "edad":20,
    "hobbies": ["Futbol", "Nadar", "Jugar"]
}

#1.- Primera forma
print(f'Nombre de la persona: {persona["edad"]}')
print(f'Segundo Hobby: {persona["hobbies"][1]}')

#2.- Segunda forma
# print(persona["cursos"])
"""Get -> Busca el valor con la clave mencionada, retorna el valor"""
print(persona.get("cursos"))
