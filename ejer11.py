n = int(input("N: "))

if n < 0:
    print("0! = 1")
elif n == 0:
    print("0! = 1")
else:
    factorial = 1
    expresion = "1"
    
    for i in range(2, n + 1):
        factorial *= i
        expresion += f" x {i}"
    
    print(f"{n}! = {expresion} = {factorial}")
