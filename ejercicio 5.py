while True:
    numero = int(input("Introduce un número entre 0 y 20 para calcular su factorial: "))
    
    while numero < 0 or numero > 20:
        print("El número debe estar entre 0 y 20.")
        numero = int(input("Introduce un número entre 0 y 20 para calcular su factorial: "))
    
    factorial = 1
    i = 1
    
    while i <= numero:
        factorial *= i
        i += 1
    

    print(f"El factorial de {numero} es {factorial}.")
    

    respuesta = input("¿Quieres calcular el factorial de otro número? (s/n): ").strip().lower()
    if respuesta != 's':
        print("Fin del programa.")
        break
