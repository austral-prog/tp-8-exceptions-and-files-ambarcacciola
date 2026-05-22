def merge_files(archivo1, archivo2, archivo_salida):
    with open(archivo1, 'r') as archi1:
        contenido1 = archi1.read()

    with open(archivo2, 'r') as archi2:
        contenido2 = archi2.read()

    with open(archivo_salida, 'w') as salida:
        salida.write(contenido1 + contenido2)
