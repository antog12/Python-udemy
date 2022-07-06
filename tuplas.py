# la tupla no es modificable

# definir una tupla
frutas= ("manzana", "pera", "uva")
#saber el largo de una tupla
print(len(frutas))
#acceder a un elemento de la tupla
print(frutas[1])

#indice inverso
print(frutas[-1])

#accedera un rango de valores
print(frutas[1:3])

# si quiero una tupla con un solo elemento debo ponerlo una coma al final

verduras=("zanahoria",)
print(verduras)

#recorrer una tupla
for fruta in frutas:
    print(fruta, end=" ")# con el end le digo que se ponga en horizontal separado por espacios
#cambiar un valor de la tupla
#frutas[0]= "naranja" # no podemos cambiar un valor de una tupla
#print(frutas)

#para modificar podemos cambiar la tupla a una lista, una vez modificada, la pasamos de nuevoa tupla

frutaLista= list(frutas)#convierto la tupla en una lista
frutaLista[0]= "naranja"
frutas= tuple(frutaLista)#convierto la lista en una tupla
print("\n",frutas)

#eliminar la tupla
#del frutas
#print(frutas)# me sale erro de no existe la tupla

#dada la siguiente tupla crear una lista que solo incluya los numeros menores a 5
tupla=(13,1,8,3,2,5,8)
lista=[]
for numero in tupla:
    if numero < 5:
        lista.append(numero)
print(lista)







