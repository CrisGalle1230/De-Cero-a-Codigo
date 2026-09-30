# Función separada para cumplir con la regla del ejercicio
def calcular_valor_total(inventario_actual):
    total = 0
    # Recorre todos los productos para multiplicar precio x cantidad
    for producto, datos in inventario_actual.items():
        total += datos["precio"] * datos["cantidad"]
    return total

# 1. Diccionario principal que actúa como base de datos
inventario = {}

# 2. Menú repetitivo
while True:
    print("\n--- Sistema de Inventario ---")
    print("1. Agregar o reponer producto")
    print("2. Vender producto")
    print("3. Listar inventario")
    print("4. Ver valor total del inventario")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del producto: ").lower()
        try:
            cantidad = int(input("Cantidad a ingresar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
                continue
                
            # Si el producto ya existe, solo sumamos el stock
            if nombre in inventario:
                inventario[nombre]["cantidad"] += cantidad
                print(f"Stock actualizado. {nombre}: {inventario[nombre]['cantidad']}")
            # Si no existe, pedimos el precio y lo creamos
            else:
                precio = float(input("Precio del producto: "))
                if precio < 0:
                    print("Error: El precio no puede ser negativo.")
                    continue
                # Estructura de diccionarios anidados
                inventario[nombre] = {"precio": precio, "cantidad": cantidad}
                print(f"Producto '{nombre}' agregado correctamente.")
                
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")
            
    elif opcion == "2":
        nombre = input("Nombre del producto a vender: ").lower()
        
        # Validar regla de negocio: existencia
        if nombre not in inventario:
            print("Error: El producto no existe en el inventario.")
        else:
            try:
                cantidad_vender = int(input("Cantidad a vender: "))
                
                # Validar regla de negocio: stock suficiente (no negativo)
                if cantidad_vender <= 0:
                    print("Error: La cantidad a vender debe ser mayor a 0.")
                elif inventario[nombre]["cantidad"] >= cantidad_vender:
                    inventario[nombre]["cantidad"] -= cantidad_vender
                    print(f"Venta realizada. Stock de {nombre}: {inventario[nombre]['cantidad']}")
                else:
                    print(f"Error: Stock insuficiente. Solo hay {inventario[nombre]['cantidad']} unidades disponibles.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
                
    elif opcion == "3":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\n--- Productos en stock ---")
            # Recorrer diccionario mostrando llaves y valores
            for nombre, datos in inventario.items():
                print(f"- {nombre.capitalize()}: {datos['cantidad']} unds | Precio: ${datos['precio']}")
                
    elif opcion == "4":
        # Llamado a la función encapsulada
        total_plata = calcular_valor_total(inventario)
        print(f"\nValor total del inventario: ${total_plata:.2f}")
        
    elif opcion == "5":
        print("Cerrando sistema...")
        break
        
    else:
        print("Opción inválida.")