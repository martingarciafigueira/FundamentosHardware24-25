temperatura = float(input("Introduce la temperatura: "))
if temperatura < 10:
    print("Hace frío.")
elif 10 <= temperatura <= 25:
    print("Está templado.")
else:
    print("Hace calor.")
