n = int(input("Introduce un valor para n (entre 1 y 9): "))

while n < 1 or n > 9:
    print("El valor de n debe estar entre 1 y 9.")
    n = int(input("Introduce un valor para n (entre 1 y 9): "))

x = 0

while x <= n:
    resultado = n ** x
    print(f"{n}^{x} = {resultado}")
    x += 1
