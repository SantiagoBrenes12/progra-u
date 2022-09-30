n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

suma = n1 + n2
resta = n1 - n2
division = "Un numero no puede ser dividido entre 0" if n2 == 0 else (n1 / n2)
multiplicacion = n1 * n2

print(
    f"El resultado de 12la suma es: {suma}",
    f"El resultado de la resta es: {resta}",
    f"El resultado de la division es: {division}",
    f"El resultado de la multiplicacion es: {multiplicacion}",
    sep="\n",
)


hola = "hola"
