productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1]
}

def stock_marca(marca):
    total = 0
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            encontrados = True
            unidades = stock.get(modelo, [0, 0])[1]
            print(f"{modelo}: {unidades} unidades")
            total += unidades
    if encontrados:
        print("El stock es:", total)
    else:
        print("Marca no encontrada.")

def busqueda_precio(p_min, p_max):
    lista = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            lista.append(f"{marca}--{modelo}")
    if lista:
        lista.sort()
        print("Los notebooks entre los precios consultas son:", lista)
    else:
        print("No hay notebooks en ese rango de precios.")

def ordenar_productos():
    if not productos:
        print("No hay notebook disponibles para mostrar")
        return
    print("------- Listado de Notebooks Ordenados --------")
    lista = []
    for modelo, datos in productos.items():
        marca = datos[0]
        ram = datos[2]
        capacidad = datos[4]
        lista.append(f"{marca} - {modelo} - {ram} - {capacidad}")
    for linea in sorted(lista):
        print(linea)
    print("------------------------------------------------")

while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Listado de productos.")
    print("4. Salir.")
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        marca = input("Ingrese marca a consultar: ")
        stock_marca(marca)
    elif opcion == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
                break
            except:
                print("Debe ingresar valores enteros!!")
            finally:
                pass
    elif opcion == "3":
        ordenar_productos()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")
