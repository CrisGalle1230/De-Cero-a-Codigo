number = int(input("Número: "))

if number < 2:
    print("Error: El número debe ser entero y mayor o igual a 2.")
else:
    es_primo = True
    divisor_encontrado = None
    
    for i in range(2, number):
        if number % i == 0:
            es_primo = False
            divisor_encontrado = i
            break
    
    if es_primo:
        print(f"{number} es PRIMO.")
    else:
        print(f"{number} NO es primo.")
        print(f"Divisor encontrado: {divisor_encontrado}")