# Pedimos las 3 puntuaciones al usuario
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print("") # Espacio en blanco para separar la entrada de la salida

# PASO 1: Encontrar el mayor
# Asumimos temporalmente que 'a' es el mayor, y lo comparamos con los demás
mayor = a

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

print(f"Mayor puntuacion: {mayor}")

# PASO 2: Verificar si hay empate en el primer lugar
# Comprobamos si al menos un par de variables son iguales y además son el número mayor
empate_ab = (a == mayor and b == mayor)
empate_ac = (a == mayor and c == mayor)
empate_bc = (b == mayor and c == mayor)

# Si cualquiera de esos empates es verdadero, imprimimos el mensaje
if empate_ab or empate_ac or empate_bc:
    print("Hay empate en el primer lugar.")

