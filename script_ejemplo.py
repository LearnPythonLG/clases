
nombre = input("Ingrese su nombre: ")

with open('registros.txt', 'a') as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write("\n")
    