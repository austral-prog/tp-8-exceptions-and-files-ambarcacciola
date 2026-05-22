def csv_to_dict(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().strip()

    if not contenido:
        return []

    lineas = contenido.split('\n')

    encabezado = lineas[0].strip().split(',')

    lista_resultado = []

    for i in range(1, len(lineas)):
        linea_limpia = lineas[i].strip()

        if linea_limpia:
            datos_fila = linea_limpia.split(',')

            diccionario_persona = {
                'name': datos_fila[0],
                'age': int(datos_fila[1]),
                'city': datos_fila[2]
            }
            lista_resultado.append(diccionario_persona)

    return lista_resultado
