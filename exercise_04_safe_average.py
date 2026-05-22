def safe_average(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    suma_total = 0.0
    cantidad_numeros = 0

    for linea in lineas:
        texto_limpio = linea.strip()

        if texto_limpio:
            try:
                numero = float(texto_limpio)
                suma_total += numero
                cantidad_numeros += 1
            except ValueError:
                pass

    if cantidad_numeros == 0:
        raise ValueError("no valid numbers")

    return suma_total / cantidad_numeros
