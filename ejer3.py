#CALCULADORA DE PINTURA
ancho_pared = float(input("Ancho en metros:"))

alto_pared = float(input("Alto en metros:"))

area_total = (ancho_pared * alto_pared)

pintura_estimada = (area_total / 8)

print(f"""Area: {area_total:.2f} m2
Pintura estimada: {pintura_estimada:.2f} litros.""")

