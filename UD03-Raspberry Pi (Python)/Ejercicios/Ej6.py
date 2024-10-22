while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
