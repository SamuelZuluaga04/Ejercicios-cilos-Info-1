n = int(input("Introduce un valor para n (entero positivo): "))


while n <= 0:
    print("El valor de n debe ser un entero positivo.")
    n = int(input("Introduce un valor para n (entero positivo): "))


suma = 0
i = 1


while i <= n:
    if i % 2 != 0:  
        suma += i
    i += 1


print(f"La suma de los números impares comprendidos entre 1 y {n} es: {suma}")
