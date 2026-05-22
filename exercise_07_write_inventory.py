def write_inventory(nombre_archivo, inventario):
    items_ordenados = sorted(inventario.keys())
    with open(nombre_archivo, 'w') as archivo:
        for item in items_ordenados:
            cantidad = inventario[item]
            # Escribimos con el formato item:cantidad y el salto de línea al final
            archivo.write(f"{item}:{cantidad}\n")
