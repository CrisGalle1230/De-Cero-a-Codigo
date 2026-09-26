print("Sumar - Restar - Multiplicar - Dividir - Elevar")

a = float(input("A: "))
b = float(input("B: "))
operacion = input("Operacion: ")

if operacion == "+":
    resultado = a + b
    print(f"Resultado : {resultado:}")
elif operacion == "-":
    resultado = a - b
    print(f"Resultado : {resultado}")
elif operacion == "*":
    resultado = a * b
    print(f"Resultado : {resultado}")
elif operacion == "**":
    resultado = a ** b
    print(f"Resultado : {resultado}")
elif operacion == "/":
    if b == 0:
        print("Error: No se puede dividir entre 0")
    else:
        resultado = a / b
        print(f"Resultado : {resultado}")
else: 
    print("Error: Ninguna de estas operaciones son validas")