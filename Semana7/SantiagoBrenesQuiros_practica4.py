# Fizz buzz


numero = int(input("Ingrese un numero entre 1 y 20: "))

fizbuzz = ""

for i in range(1, numero + 1):
    # if (i % 3) == 0 and (i % 5) == 0:
    #     print("3,5", i)
    #     fizbuzz += "fizzbuzz"
    #     print(fizbuzz)
    if i % 3 == 0:
        print("3", i)
        fizbuzz += "fizz"
        print(fizbuzz)

    if i % 5 == 0:
        print("5", i)
        fizbuzz += "buzz"
        print(fizbuzz)


print("fizzbuzzfizzfizzbuzzfizzfizzbuzz" == "fizzbuzzfizzfizzbuzzfizzfizzbuzz")
