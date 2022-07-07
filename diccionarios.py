# tienen la forma de llaves y valores
diccionario={
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System",
}
print(diccionario)
print(len(diccionario))
#acceder a un elemento del diccionario
print(diccionario["IDE"])
#otra forma de acceder a un elemento del diccionario
print(diccionario.get("OOP"))
#modificar elemento del diccionario
diccionario["IDE"]="integrated development environment"
print(diccionario)

#recorrer un diccionario
for llave, valor in diccionario.items():# con items() podemos recorrer un diccionario separando llave y valor
    print(llave,":", valor)

#recorrer solo las llaves
for llave in diccionario.keys():
    print(llave)# se recuperan solo las llaves

#recorrer solo los valores
for valor in diccionario.values():
    print(valor)# se recuperan solo los valores

#comprobar si un elemento esta en el diccionario
print("DBMS" in diccionario)

#agregar un elemento al diccionario
diccionario["PK"]="Primary key"
print(diccionario)

#eliminar un elemento del diccionario
del diccionario["PK"]
print(diccionario)

#eliminar todos los elementos del diccionario
diccionario.clear()
print(diccionario)

#eliminar el diccionario por completo
del diccionario
print(diccionario)#sale error porque no existe el diccionario