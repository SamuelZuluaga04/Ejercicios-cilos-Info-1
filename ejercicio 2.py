
suma_notas = 0
contador_notas = 0


numero_notas = int(input("Introduce el número de notas: "))


while numero_notas <= 0:
    print("El número de notas debe ser mayor que 0.")
    numero_notas = int(input("Introduce el número de notas: "))


while contador_notas < numero_notas:
    nota = float(input(f"Introduce la nota {contador_notas + 1} (de 0 a 5): "))
    
    
    while nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5.")
        nota = float(input(f"Introduce la nota {contador_notas + 1} (de 0 a 5): "))
    
    
    suma_notas += nota
    contador_notas += 1


promedio = suma_notas / numero_notas


print(f"El promedio de las notas es: {promedio:.2f}")
