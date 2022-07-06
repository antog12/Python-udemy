"""cadena = "hola"

for i in cadena:
    print(i)
else:
    print("fin del ciclo for")"""
#---------------------------------------

"""pais= "Holanda"
for i in pais:
    if i == "a":
        print("la letra a esta en la posicion", pais.index("a"))
    else:
        print("fin del ciclo for")"""
#---------------------------------------


"""for letra in "Holanda":
    if letra == "a":
        print(f'letra encontrada: {letra}')
        break # rompemos el ciclo for una vez que encuentre lo que estoy buscando.

else:
    print("fin del ciclo for")"""
#---------------------------------------

"""for i in range(6):
    if i%2 == 0:
        print("Valor: ",i)"""
#---------------------------------------
"""for i in range(2,10,2):
    print(i)"""
#---------------------------------------

for i in range (2):
    nombre= input("Ingrese su nombre: ")
    apellido= input("Ingrese su apellido: ")
    print(f"Hola {nombre} {apellido}") # f es una forma de concatenar strings
else:
    print("fin del ciclo for")
