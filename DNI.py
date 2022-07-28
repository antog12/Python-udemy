# calcular la etra de tu dni

letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"

dni=int(input("Ingrese su dni: "))
resto=dni%23
print("el resto es: ",resto)
resultado=letras_dni[resto]
print("Su letra es: ",resultado)