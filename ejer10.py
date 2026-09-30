ahorroMensual = int((input("Ahorro Mensual: ")))

meses = int(input("Meses: "))

if meses <= 0: 
    print("Error: La cantidad de meses debe ser un número positivo (mayor a 0).")
else:
    ahorro_acumulado = 0 
    
    for mes in range(1, meses + 1):
        ahorro_acumulado += ahorroMensual
        print (f"Mes {mes}: {ahorro_acumulado}")
    
    print(f"Total: {ahorro_acumulado}")

