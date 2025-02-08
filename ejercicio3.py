# ejercicio3.py

cadena = input("Ingrese una cadena de texto: ")
cadena_simple = cadena.replace(" ", "").lower()  # esta linea la usé para otros ejercicios, basicamente la idea es que si el usuario ingresa un espacio lo elimine y pase la cadena a minusculas con el lower.
if cadena_simple == cadena_simple[::-1]:  # cadena_simple[::-1] es basicamente el comando para recorer la cadena de derecha a izquierda, por lo quee despues verifica si es igual a la cadena original.
    print("Si")
else:
    print("No")
