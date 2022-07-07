# set es una coleccion sin orden y sin indices

planetas={"mercurio", "venus", "tierra"}
print(planetas)

#largo del set

print(len(planetas))

# revisar si un elemento esta en el set

print("mercurio" in planetas)

#agregar un elemento al set

print(planetas.add("marte"))
print(planetas)

#no soprta duplicados
planetas.add("mercurio")
print(planetas)# no se agrega el elemento

#elimir un elemento del set y puede arrojar un error sino encuentra la llave
planetas.remove("mercurio")
print(planetas)

#otra forma de eliminar es con discard y no sale error
planetas.discard("marte")
print(planetas)

#limpiar todos los elementos del set
planetas.clear()
print(planetas)

#eliminar el set
del planetas




