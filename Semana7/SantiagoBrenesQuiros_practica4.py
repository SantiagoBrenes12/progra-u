# Fizz buzz


numero = int(input("Ingrese un numero entre 1 y 20: "))

fizbuzz = ""

for i in range(1, numero + 1):
    if (i % 3) == 0 and (i % 5) == 0:
        fizbuzz += "fizzbuzz"
    if i % 3 == 0:
        fizbuzz += "fizz"
    if i % 5 == 0:
        fizbuzz += "buzz"

print(fizbuzz)