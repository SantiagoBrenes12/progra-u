"""
    Tarea #1
    Link github: https://github.com/SantiagoBrenes12/progra-u/blob/main/Semana4/SantiagoBrenesQuiros_G5_Tarea1.py
"""

CCSS_CONTRIBUTION = 0.09
BANCO_POPULAR_CONTRIBUTION = 0.01
ASOCIACION_SOLIDARISTA_CONTRIBUTION = 0.03

id = input("Porfavor ingrese su cedula: ")
name = input("Porfavor ingrese su nombre: ")
gross_pay = int(input("Porfavor ingrese su salario bruto: "))

ccss_deduction = int(gross_pay * CCSS_CONTRIBUTION)
banco_popular_deduction = int(gross_pay * BANCO_POPULAR_CONTRIBUTION)
asociacion_solidarista_deduction = int(gross_pay * ASOCIACION_SOLIDARISTA_CONTRIBUTION)

total_deductions = int(
    (ccss_deduction + banco_popular_deduction + asociacion_solidarista_deduction)
)
net_salary = gross_pay - total_deductions

print(
    "",
    f"Salario bruto: {gross_pay:,}",
    f"9.5% CCSS: {ccss_deduction:,}",
    f"1% Banco Popular: {banco_popular_deduction:,}",
    f"3% Asociacion Solidarista: {asociacion_solidarista_deduction:,}",
    f"Total de deducciones: {total_deductions:,}",
    f"Salario Neto: {net_salary:,}",
    sep="\n",
)
