# ejercicio1.py

num = input("Ingrese un número entero: ")
suma = 0
for digito in num:
    if digito.isdigit():  
        suma += int(digito)

print("La suma de los dígitos del entero es:", suma)





