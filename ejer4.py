#CALCULADORA CUENTA COMPARTIDA
total_cuenta = float(input("Cuenta:"))

porcentaje_propina = float((input("Propina %:"))) / 100

num_personas = int(input("Personas:"))

valor_propina = (total_cuenta * porcentaje_propina)

total_a_pagar = (total_cuenta + valor_propina)

pago_persona =(total_a_pagar / num_personas)

print(f"""Propina: {valor_propina:.2f}\n
Total: {total_a_pagar:.2f}\n
Cada persona paga: {pago_persona:.2f}""")

