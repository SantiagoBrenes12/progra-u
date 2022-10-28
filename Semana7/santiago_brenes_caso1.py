""""

    Aclarar que este algoritmo se explica como si fuera solo un lote. 
    El mismo aplica para lote 1 y dos. Se resalta la formula para
    el area del cuadrado y del rectangulo.

    1. El problema contará con operaciones basadas en la medida de un area,
       que obtenemos con el largo. Esta medida no esta establecida
       en el problema dado, por lo tanto:

        Para obtener el area del lote:
         - Obtener el largo por medio de input, casteado a float,
           se guardara en {largo_lote} : float
         - En el caso del rectangulo, obtener el ancho dividiendo el largo entre 2, se guardara
           en {ancho_lote} : float

        Formula cuadrado:
          - {largo_lote**2} : float
        Formula rectangulo:
         -  {largo_lote*ancho_lote} : float

         - El area se guardara en {area_lote} : float

    2. El problema tambien pide que brinde el precio basado en el 
       precio por metro, que tampoco es brindado, por lo que tambien 
       se tiene que solicitar, por lo tanto:

        Para obtener el precio del lote:
         -  Obtener el precio por metro cuadrado, se guardara en
            {precio_por_metro_cuadrado} : float 
         -  Multiplicar el area del lote por el precio por metro cuadrado,
            se guardara en {precio_lote} : float

    3. Una vez con todos los resultados, se muestra el precio del lote uno y dos, por medio de un input.
"""

# Lote 1 - Rectangular
largo_lote_uno = float(input("Porfavor ingrese el largo del primer lote en metros: "))
precio_por_metro_cuadrado_lote_uno = float(
    input("Porfavor ingrese el precio por metro cuadrado del primer lote (colones): ")
)
ancho_lote_uno = largo_lote_uno / 2
area_lote_uno = largo_lote_uno * ancho_lote_uno

precio_lote_uno = area_lote_uno * precio_por_metro_cuadrado_lote_uno


# Lote 2 - Cuadrado
largo_lote_dos = float(input("Porfavor ingrese el largo del primer lote en metros: "))
precio_por_metro_cuadrado_lote_dos = float(
    input("Porfavor ingrese el precio por metro cuadrado del primer lote (colones): ")
)
area_lote_dos = largo_lote_dos**2

precio_lote_dos = area_lote_dos * precio_por_metro_cuadrado_lote_dos


# Se imprime el resultado
print(
    "",
    f"El precio del primer lote, con un area de {area_lote_uno} metros cuadrados es: {precio_lote_uno}",
    "-------------------------------------------------------------------------------------------------",
    f"El precio del segundo lote, con un area de {area_lote_dos} metros cuadrados es: {precio_lote_dos}",
    "",
    sep="\n",
)
