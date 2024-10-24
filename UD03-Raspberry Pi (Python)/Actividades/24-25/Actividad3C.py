numero1 = int(input("Dame el primer número"))
numero2 = int(input("Dame el segundo número"))

# if numero1 > 0 and numero2 > 0:
#     print("Los dos números son positivos")
# else:
#     if numero1 > 0 or numero2 >0:
#         print("Uno de los dos números es positivo")
#     else:
#         print("Los dos números son negativos")

if numero1 > 0 and numero2 > 0:
    print("Los dos números son positivos")
elif numero1 > 0 or numero2 > 0:
    print("Uno de los dos números es positivo")
else:
    print("Los dos números son negativos")