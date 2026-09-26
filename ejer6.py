edad = int((input("Edad: ")))

if edad < 0:
    print("Edad No valida")
elif edad <= 11:
    print("Infancia")
elif edad <= 17:
    print("Adolescente")
elif edad <= 59:
    print("Adultez")
else:
    print("Adulto Mayor")