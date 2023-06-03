# Hallar cuantos son multiplos de 3 y de 5, de una lista
# si existe un multiplo que sea de 3 y 5 a la vez, no debe contabilizar

numeros = [1,2,5,9,12,15,10,34,67]

multiplo_tres = 0
multiplo_cinco = 0

for index,numero in enumerate(numeros):
    if numero % 3 == 0 and numero % 5 == 0:
        continue
    else: 
        if numero % 3 == 0:
            multiplo_tres += 1
        if numero % 5 == 0:
            multiplo_cinco += 1
        
print(multiplo_tres)
print(multiplo_cinco)

