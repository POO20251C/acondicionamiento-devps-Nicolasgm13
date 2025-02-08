# ejercicio2.py

cadena = input("Ingrese una cadena de texto: ").lower()
contador = 0

for letra in cadena:
    if letra in "aeiou":
        contador += 1

print(contador)
