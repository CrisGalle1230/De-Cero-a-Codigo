try:
    entrada = input("Notas: ")

    # 1. Separar el texto en una lista de cadenas
    notas_texto = entrada.split(",")

    # 2. Bucle para convertir cada fragmento de texto a número decimal (float)
    notas = []
    for nota_str in notas_texto:
        notas.append(float(nota_str))

    # 3. Operaciones de agregación
    promedio = sum(notas) / len(notas)
    nota_mayor = max(notas)
    nota_menor = min(notas)

    # 4. Conteo de aprobadas
    aprobadas = 0
    for nota in notas:
        if nota >= 3.0:
            aprobadas += 1

    # 5. Salida de datos con formato de dos decimales para el promedio
    print(f"Promedio: {promedio:.2f}")
    print(f"Mayor: {nota_mayor}")
    print(f"Menor: {nota_menor}")
    print(f"Aprobadas: {aprobadas}")

except ValueError:
    print("Error: Asegúrate de separar las notas por comas y usar puntos para los decimales (ej. 4.5, 3.2).")