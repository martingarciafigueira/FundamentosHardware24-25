edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres un niño/a")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 70:
    print("Eres un adulto") 
elif edad >= 70:
    print("Eres un anciano")
else:
    print("Edad incorrecta")            
