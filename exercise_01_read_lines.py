# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    lista_limpia = []
    with open(filename, 'r') as archivo:
        for linea in archivo:
            linea_procesada = linea.strip()
            if linea_procesada:
                lista_limpia.append(linea_procesada)
    return lista_limpia

