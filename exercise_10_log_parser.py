def parse_log(nombre_archivo):
    diccionario_logs = {}

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea_limpia = linea.strip()

        if linea_limpia:
            if ":" not in linea_limpia:
                raise ValueError("invalid log line")

            partes = linea_limpia.split(':', 1)
            nivel = partes[0].strip()
            mensaje = partes[1].strip()

            if nivel not in diccionario_logs:
                diccionario_logs[nivel] = []
            diccionario_logs[nivel].append(mensaje)

    return diccionario_logs
