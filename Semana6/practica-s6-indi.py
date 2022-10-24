# ejercicio 1

litro_super = 822
litro_regular = 804
litro_diesel = 724

tipo_litro = int(
    input(
        "Porfavor ingrese el tipo de gasolina que desea, ingrese un numero:\n (1) Super\n (2) Regular\n (3) Diesel\n"
    )
)
cantidad_litros = int(input("Porfavor ingrese la cantidad de litros: "))

monto_total = 0

if tipo_litro is 1 or tipo_litro is 2 or tipo_litro is 3:
    if tipo_litro == 1:
        monto_total = cantidad_litros * litro_super
    elif tipo_litro == 2:
        monto_total = cantidad_litros * litro_regular
    else:
        monto_total = cantidad_litros * litro_diesel
    print(f"El precio a pagar es: {monto_total}")
else:
    print("No existe este tipo de gasolina.")
