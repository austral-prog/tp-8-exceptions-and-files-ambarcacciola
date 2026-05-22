def grades_stats(nombre_archivo):
    resultado = {}

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea_limpia = linea.strip()

        if linea_limpia:
            partes = linea_limpia.split(':')
            estudiante = partes[0]

            lista_notas_texto = partes[1].split(',')

            notas_numeros = []
            for nota in lista_notas_texto:
                notas_numeros.append(float(nota))

            promedio = sum(notas_numeros) / len(notas_numeros)
            maximo = max(notas_numeros)
            minimo = min(notas_numeros)

            resultado[estudiante] = (promedio, maximo, minimo)

    return resultado
