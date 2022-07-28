#Te pregunta quién eres y sólo si eres la persona indicada te
#pregunta la contraseña.

while True:
    nombre=input("¿Quién eres? ")
    if nombre=="Juan":
        contraseña=input("Ingrese su contraseña: ")
        if contraseña=="123":
            print("Bienvenido",nombre)
            break
        else:
            print("Contraseña incorrecta")
    else:
        print("No eres",nombre)
        continue
    print("Gracias por visitarnos")
    break