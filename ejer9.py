while True:
    # 1. Ejecutamos tu programa principal
    numero = int(input("Ingresa un número para ver su tabla: "))

    print(f"\n--- Tabla del {numero} ---")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
    # 2. Creamos el "botón" de repetir
    repetir = input("\n¿Quieres ver otra tabla? (si/no): ").strip().lower()
    
    # 3. Verificamos la respuesta
    if repetir != "si":
        print("¡Programa terminado!")
        break  # El break destruye el bucle 'while' y finaliza todo