# Estructura de datos principal: diccionario de estanterías.
almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5}, {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0}, {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8}, {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

# Función para agregar una estantería
def agregar_estanteria(nombre_estanteria):
    if nombre_estanteria not in almacen:
        almacen[nombre_estanteria] = []
    else:
        print("La estantería ya existe.")

# Gestión de Entrada de Productos
def agregar_producto(nombre_producto, cantidad, precio, nombre_estanteria):
    # Verificamos si la estantería existe
    if nombre_estanteria not in almacen:
        agregar_estanteria(nombre_estanteria)
    
    # Agregamos el producto como un diccionario en la lista de la estantería
    producto = {"nombre": nombre_producto, "cantidad": cantidad, "precio": precio}
    almacen[nombre_estanteria].append(producto)
    print(f"Producto '{nombre_producto}' agregado correctamente a '{nombre_estanteria}'.")

# Gestión de Salida de Productos
def retirar_producto(nombre_producto, cantidad, nombre_estanteria):
    if nombre_estanteria in almacen:
        for producto in almacen[nombre_estanteria]:
            if producto["nombre"] == nombre_producto:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"{cantidad} unidades de '{nombre_producto}' retiradas de '{nombre_estanteria}'.")
                    return
                else:
                    print("Error: cantidad insuficiente.")
                    return
    print(f"Producto '{nombre_producto}' no encontrado en '{nombre_estanteria}'.")

# Verificar Disponibilidad de Productos
def verificar_disponibilidad(nombre_producto):
    for nombre_estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre_producto:
                print(f"{nombre_producto} disponible en '{nombre_estanteria}': {producto['cantidad']} unidades")
                return
    print(f"{nombre_producto} no se encuentra en el almacén.")

# Verificar el Estado del Almacén
def estado_almacen():
    total_inventario = 0
    valor_total = 0
    for nombre_estanteria, productos in almacen.items():
        cantidad_estanteria = sum(p["cantidad"] for p in productos)
        valor_estanteria = sum(p["cantidad"] * p["precio"] for p in productos)
        total_inventario += cantidad_estanteria
        valor_total += valor_estanteria
        print(f"Estantería '{nombre_estanteria}': {cantidad_estanteria} productos, valor total: {valor_estanteria}")
    print(f"Inventario total: {total_inventario} productos, valor total del almacén: {valor_total}")

# Transferencia de Productos entre Estanterías
def transferir_producto(nombre_producto, cantidad, estanteria_origen, estanteria_destino):
    if estanteria_origen not in almacen or estanteria_destino not in almacen:
        print("Error: una de las estanterías no existe.")
        return

    # Buscar el producto en la estantería de origen
    for producto in almacen[estanteria_origen]:
        if producto["nombre"] == nombre_producto:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                agregar_producto(nombre_producto, cantidad, producto["precio"], estanteria_destino)
                print(f"{cantidad} unidades de '{nombre_producto}' transferidas de '{estanteria_origen}' a '{estanteria_destino}'.")
                return
            else:
                print("Error: cantidad insuficiente en la estantería de origen.")
                return
    print(f"Producto '{nombre_producto}' no encontrado en '{estanteria_origen}'.")

# Optimización del Inventario (BONUS)
def optimizar_inventario():
    estanteria_mayor_valor = None
    estanteria_menor_productos = None
    mayor_valor = 0
    menor_cantidad = float('inf')

    for nombre_estanteria, productos in almacen.items():
        valor_estanteria = sum(p["cantidad"] * p["precio"] for p in productos)
        cantidad_estanteria = sum(p["cantidad"] for p in productos)

        if valor_estanteria > mayor_valor:
            mayor_valor = valor_estanteria
            estanteria_mayor_valor = nombre_estanteria

        if cantidad_estanteria < menor_cantidad:
            menor_cantidad = cantidad_estanteria
            estanteria_menor_productos = nombre_estanteria

    print(f"Estantería con mayor valor acumulado: {estanteria_mayor_valor} con valor {mayor_valor}")
    print(f"Estantería con menos productos: {estanteria_menor_productos} con {menor_cantidad} productos")

# Ejemplo de cómo utilizar las funciones
agregar_estanteria("Estantería E")
agregar_producto("Galletas", 100, 1.2, "Estantería E")
retirar_producto("Café Molido", 10, "Estantería C")
verificar_disponibilidad("Aceitunas Verdes")
estado_almacen()
transferir_producto("Té Verde", 5, "Estantería C", "Estantería A")
optimizar_inventario()
