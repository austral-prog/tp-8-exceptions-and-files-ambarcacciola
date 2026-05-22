def read_sales(filename):
    sales_dict = {}
    with open(filename, 'r') as archivo:
        contenido = archivo.read().strip()
    ventas = contenido.split(';')
    for venta in ventas:
        if venta:
            producto, cantidad_str = venta.split(':')
            cantidad = float(cantidad_str)

            if producto not in sales_dict:
                sales_dict[producto] = []

            sales_dict[producto].append(cantidad)

    return sales_dict


def process_sales(data):
    for producto, cantidad in data.items():
        total = sum(cantidad)
        hmt = len(cantidad)
        average = total / hmt
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${average:.2f}")
