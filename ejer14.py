texto = input("Texto: ")

# 1. Normalización inicial: pasar a minúsculas
texto_limpio = texto.lower()

# Reemplazo de tildes para evitar que rompan la comparación
reemplazos = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
for vocal_con_tilde, vocal_sin_tilde in reemplazos:
    texto_limpio = texto_limpio.replace(vocal_con_tilde, vocal_sin_tilde)

# 2. Filtrado usando comprensión de listas y join
# isalnum() verifica que sea alfabético o numérico, ignorando signos y espacios
texto_normalizado = "".join(caracter for caracter in texto_limpio if caracter.isalnum())

# 3. Slicing para invertir el texto
texto_invertido = texto_normalizado[::-1]

# 4. Decisión final
if texto_normalizado == texto_invertido:
    print("Es palindromo.")
else:
    print("No es palindromo.")