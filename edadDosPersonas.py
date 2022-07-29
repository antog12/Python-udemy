#escribir un programa que diga cque persona es mayor de edad

persona1=int(input("Ingrese la edad de la persona 1: "))
persona2=int(input("Ingrese la edad de la persona 2: "))

if persona1>persona2:
    print("La persona 1 es mayor de edad")
elif persona1<persona2:
    print("La persona 2 es mayor de edad")
else:
    print("Ambas personas tienen la misma edad")