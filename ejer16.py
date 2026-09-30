notas = []

# 1. Bucle de validación continua
while len(notas) < 3:
    try:
        # El texto dinámico muestra qué número de nota se está pidiendo
        nota = float(input(f"Nota {len(notas) + 1}: "))
        
        # 2. Decisión de rango
        if 0 <= nota <= 5:
            # Si es válida, se guarda y el tamaño de la lista aumenta
            notas.append(nota)
        else:
            print("-> invalida. La nota debe estar entre 0 y 5.")
            
    except ValueError:
        # Prevención de ruptura si el usuario ingresa texto
        print("-> invalida. Por favor ingresa un número (usa punto para decimales).")

# 3. Operaciones matemáticas
promedio = sum(notas) / len(notas)

# 4. Asignación de estado
if promedio < 3.0:
    estado = "Reprobado"
elif 3.0 <= promedio < 4.5:
    estado = "Aprobado"
else:
    estado = "Excelente"

# 5. Salida de datos formateada
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")