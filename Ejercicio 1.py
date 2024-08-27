a = int(input("Ingresar número: "))
b = int(input("Ingresar número 2: "))


resultado = 0


contador = b

# Multiplicar usando solo sumas
while contador > 0:
    resultado += a
    contador -= 1

# Ajustar el signo del resultado si es necesario
if (a < 0) != (b < 0):
    resultado = -resultado


print(f"La multiplicación de {a} y {b} es: {resultado}")
