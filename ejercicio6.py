# ejercicio6.py

entrada = input("Ingrese números separados por espacios: ").split()
numeros = [int(num) for num in entrada] 

print("El número maximo es:",max(numeros),"\nEl numero minimo es:",min(numeros))
