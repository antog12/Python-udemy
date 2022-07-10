def sumar(a,b):
    return a+b

resultado = sumar(5,3)
print(f"El resultado de la suma es: {resultado}")

#valores por default de los parametros
def sumar(a= 5,b=5):
    return a+b

resultado = sumar()
print(f"El resultado de la suma es: {resultado}")

#argumentos variables en python

def listarnombres(*nombres):# no se los nombres que quiero tener
    for nombre in nombres:
        print(nombre)

listarnombres("Juan","Pedro","Maria")
listarnombres("Laura","Carlos")
#vemos que se me añaden a la tupla que ya tenia

# ejercicio de funcion sumar con argumentos variables

def sumar_valores(*valores):
    total=0
    for valor in valores:
        total=total+valor
    return total

print(sumar_valores(1,2,3,4,5))

#ejercicio de multiplicar con argumentos variables

def multiplicar_valores(*valores):
    total=1
    for valor in valores:
        total=total*valor
    return total
print(multiplicar_valores(1,2,3,4,5))
