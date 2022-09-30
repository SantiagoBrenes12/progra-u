"""
Desarrolle un programa intercambie  el valor de las edades de Luis y Pedro y muestre las edades luego de realizado el intercambio.
Nota: Considere que las variables sólo pueden almacenar un valor a la vez, por lo que el asignar un nuevo valor provocará la pérdida del valor anterior.
"""

edad_luis = input("Edad de Luis : ")
edad_pedro = input("Edad de  Pedro : ")

edad_luis, edad_pedro = edad_pedro, edad_luis


print(f"La edad de Luis es: {edad_luis}\nLa edad de Pedro es: {edad_pedro}")
