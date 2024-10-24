nombre  = input("¿Cómo te llamas? ")
edad    = int(input("¿Qué edad tienes? "))

print("Hola! Encantado de conocerte,",nombre,".Veo que ya tienes",edad, "años")

if edad % 2 == 0:
    print("Veo que posees una edad par")
else:
    print("Veo que tu camino es el impar")