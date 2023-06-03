# Try Except

try:
    dividendo = input("Ingrese el dividendo")
    division = 5/0
    print(division)
except Exception as e:
    print(e.__class__)
    print("Ocurre un error, por que se esta trantando dividir")