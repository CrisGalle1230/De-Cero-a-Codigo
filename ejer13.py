frase = input("Frase: ")

# 1. Contadores iniciales
vocales = 0
consonantes = 0
digitos = 0
espacios = 0

# 2. Normalización de mayúsculas/minúsculas
frase_minusculas = frase.lower()
vocales_validas = "aeiouáéíóú"

# 3. Recorrido de caracteres
for caracter in frase_minusculas:
    # Verifica si es un espacio en blanco
    if caracter.isspace():
        espacios += 1
        
    # Verifica si es un número (0-9)
    elif caracter.isdigit():
        digitos += 1
        
    # Verifica si pertenece al alfabeto (letras)
    elif caracter.isalpha():
        # Si es una letra, revisamos si está en nuestro grupo de vocales
        if caracter in vocales_validas:
            vocales += 1
        else:
            # Si es letra pero no es vocal, obligatoriamente es consonante
            consonantes += 1

# 4. Datos de salida
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
print(f"Digitos: {digitos}")
print(f"Espacios: {espacios}")