# 1. Estado mutable inicial
saldo = 100000.0

# 2. Bucle infinito para el menú repetitivo
while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Salir")
    
    opcion = input("Opción: ")
    
    # 3. Decisiones y validaciones
    if opcion == "1":
        print(f"Saldo actual: {saldo}")
        
    elif opcion == "2":
        try:
            monto = float(input("Monto para consignar: "))
            # Validación de monto positivo
            if monto > 0:
                saldo += monto
                print(f"Consignación exitosa. Saldo: {saldo}")
            else:
                print("Error: No se aceptan montos negativos o cero.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico.")
            
    elif opcion == "3":
        try:
            monto = float(input("Monto para retirar: "))
            # Validación de monto positivo
            if monto > 0:
                # Validación de fondos suficientes
                if monto <= saldo:
                    saldo -= monto
                    print(f"Retiro exitoso. Saldo: {saldo}")
                else:
                    print("Error: Fondos insuficientes. No puedes retirar más de tu saldo.")
            else:
                print("Error: No se aceptan montos negativos o cero.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico.")
            
    elif opcion == "4":
        print("Saliendo del cajero...")
        break
        
    else:
        print("Opción inválida. Elige un número del 1 al 4.")