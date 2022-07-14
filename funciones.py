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

#funciones para listar diccionarios

def listar_diccionario(**diccionario): #ponemos ** para que sea un diccionario
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


listar_diccionario(IDE="Integrated Development Environment", PK="Python Keyword", PY="Python")
listar_diccionario(DBMS="Database Management System", SQL="Structured Query Language")


def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=["Juan","Pedro","Maria"]
desplegar_nombres(nombres)
desplegar_nombres("Carlos")
desplegar_nombres((1,2,3,4,5)) #Los pongo entre parentesis y se convierte en tupla
                                # si los pongo entre corchetes se convierte en lista

#funciones recursivas
def factorial(numero):# son funciones que se llaman a si mismas
    if numero==1:
        return 1
    else:
        return numero*factorial(numero-1)# el numero se reduce en 1 cada vez que se llama a la funcion

resultado=factorial(5)
print(f'El factorial de 5 es: {resultado}')

print("-----------------------------------------------------")

#imprimir números del 5 al 1 de manera descendente usando funciones recursivas
def imprimir_numero(numero):
    if numero==1:
        print(numero)
    else:
        print(numero)
        imprimir_numero(numero-1)

imprimir_numero(5)

print("-----------------------------------------------------")

#función que calcula el total de una factura incluyendo el IVA
def total_factura(precio,iva):
    total=precio+precio*(iva/100)
    return total

precio= float(input("Ingrese el precio sin impuesto: "))
iva= float(input("Ingrese el precio con impuesto: "))
precio_total=total_factura(precio,iva)
print(f"El precio total es: {precio_total}")

print("-----------------------------------------------------")

#convertidor de grados centígrados a fahrenheit
def centigrados_a_fahrenheit(grados_centigrados):
    fahrenheit=grados_centigrados*9/5+32
    return fahrenheit

#convertir de farhenheit a centígrados
def fahrenheit_a_centigrados(fahrenheit):
    centigrados=5/9*(fahrenheit-32)
    return centigrados

celsius=float(input("Ingrese los grados centígrados: "))
resultado=centigrados_a_fahrenheit(celsius)
print(f"{celsius} grados centígrados son {resultado} grados fahrenheit")

fahrenheit=float(input("Ingrese los grados fahrenheit: "))
resultado2=fahrenheit_a_centigrados(fahrenheit)
print(f"{fahrenheit} grados fahrenheit son {resultado2} grados centígrados")














