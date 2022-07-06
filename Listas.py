nombres= ["Juan","Karla", "Pedro", "Maria","Ricardo"]
#imprimir la lista de nombres

print(nombres)
#imprimir el primer nombre de la lista
print(nombres[0])
print(nombres[1])
print(nombres[-3])

#imrimir un rango de nombres
print(nombres[1:3])
#ir del inicio de la lista al indice( sin incluirlo)

print(nombres[:3])
# desde el indice indicado hasta el final de la lista

print(nombres[3:])

#cambiar un valor de la lista

nombres[3]= "Juanita"
print(nombres)

#iterar una lista (recorrerla)

for nombre in nombres:
    print(nombre)
else:
    print("no existen mas nombres")

#cuantos elementos tiene la lista

print(len(nombres)) # usamos la funcion len para saber cuantos elementos tiene la lista

#agregar un elemento a la lista
nombres.append("Paula")
print(nombres)

#insertar un elemento en una posicion especifica
nombres.insert(2,"Josemi")
print(nombres)

#eliminar un elemento de la lista
nombres.remove("Karla")
print(nombres)

#eliminar el ultimo elemento agregado
nombres.pop()
print(nombres)

#eliminar un indice especifico
nombres.pop(0)
print(nombres)

#borrar toda la lista
nombres.clear()
print(nombres)

#ejercicio. crea un rango de números del 2 al 6 e imprímelos
for numeros in range(2,7):
    print(numeros)
print("----------------------------------------------------")
#crea un ranfo de 3 a 10 con incrementos de 2
for numeros in range(3,11,2):
    print(numeros)
print("----------------------------------------------------")
#iterar un ranfo de 0 a 10 e imprimir numeros divisibles entre 3
for numeros in range(0,11):
    if numeros%3 == 0:
        print(numeros)