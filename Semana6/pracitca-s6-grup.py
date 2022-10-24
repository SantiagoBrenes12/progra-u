""""
1. Un corredor de Fórmula 1 requiere de un programa que le capture los tiempos realizados en cada vuelta y los tiempos utilizados en PITS, de manera que este al final le indique lo siguiente:
• Cuál es el tiempo promedio por vuelta.
• Cuál es el tiempo promedio por PITS.
• Qué porcentaje del tiempo PITS corresponde al tiempo de recorrido de una vuelta.
• Considere que son 10 vueltas y 10 entradas a PITS.
"""


tiempo_total_vueltas = 0
tiempo_total_pits = 0
porcentaje_pit_por_vuelta = 0


for i in range(1, 3):
    tiempo_vuelta = float(input(f"Ingrese el tiempo de la vuelta {i} en segundos: "))
    tiempo_pits = float(
        input(f"Ingrese el tiempo de pits en la parada {i} en segundos: ")
    )

    tiempo_total_vueltas += tiempo_vuelta
    tiempo_total_pits += tiempo_pits

    porcentaje_pit_por_vuelta = (tiempo_vuelta * tiempo_pits) / 100
    print(
        f"El tiempo en porcentaje perdido en PITS en la vuelta {i} es: {porcentaje_pit_por_vuelta}%"
    )

promedio_vueltas = tiempo_total_vueltas / 10
promedio_pits = tiempo_total_pits / 10

print(f"El promedio de tiempo por vuelta es: {promedio_vueltas} segundos")
print(f"El promedio de tiempo por pit es: {promedio_pits} segundos")
