import json
import os

ARCHIVO_JSON = "inventario_productos.json"

def cargar_productos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"productos": []}

def guardar_productos(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_productos():
    productos_iniciales = {
        "productos": [
            {"nombre": "Laptop", "categoria": "Electrónica", "precio": 1000, "stock": 15},
            {"nombre": "Teclado", "categoria": "Accesorios", "precio": 50, "stock": 30},
            {"nombre": "Mouse", "categoria": "Accesorios", "precio": 25, "stock": 50},
            {"nombre": "Monitor", "categoria": "Electrónica", "precio": 300, "stock": 20},
            {"nombre": "Webcam", "categoria": "Accesorios", "precio": 80, "stock": 25},
            {"nombre": "Auriculares", "categoria": "Accesorios", "precio": 60, "stock": 40},
            {"nombre": "Tablet", "categoria": "Electrónica", "precio": 500, "stock": 12},
            {"nombre": "Impresora", "categoria": "Electrónica", "precio": 200, "stock": 18},
            {"nombre": "Disco Duro", "categoria": "Almacenamiento", "precio": 100, "stock": 35},
            {"nombre": "Memoria USB", "categoria": "Almacenamiento", "precio": 15, "stock": 100}
        ]
    }
    guardar_productos(productos_iniciales)
    print("✓ Inventario inicializado con 10 productos")

def filtrar_por_categoria(categoria):
    datos = cargar_productos()
    productos_filtrados = [p for p in datos["productos"] if p["categoria"].lower() == categoria.lower()]
    
    if productos_filtrados:
        print(f"\n--- Productos en categoría '{categoria}' ---")
        for producto in productos_filtrados:
            print(f"• {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")
    else:
        print(f"No se encontraron productos en la categoría '{categoria}'")
    
    return productos_filtrados

def calcular_valor_total():
    datos = cargar_productos()
    valor_total = sum(p["precio"] * p["stock"] for p in datos["productos"])
    print(f"\n💰 Valor total del inventario: ${valor_total:,.2f}")
    return valor_total

def actualizar_stock(nombre_producto, nuevo_stock):
    datos = cargar_productos()
    encontrado = False
    
    for producto in datos["productos"]:
        if producto["nombre"].lower() == nombre_producto.lower():
            producto["stock"] = nuevo_stock
            encontrado = True
            print(f"✓ Stock de {producto['nombre']} actualizado a {nuevo_stock} unidades")
    
    if encontrado:
        guardar_productos(datos)
    else:
        print(f"No se encontró el producto '{nombre_producto}'")

def agregar_producto(nombre, categoria, precio, stock):
    datos = cargar_productos()
    nuevo_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    datos["productos"].append(nuevo_producto)
    guardar_productos(datos)
    print(f"✓ Producto {nombre} agregado correctamente")

def listar_productos():
    datos = cargar_productos()
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    for i, producto in enumerate(datos["productos"], 1):
        print(f"{i}. {producto['nombre']} ({producto['categoria']})")
        print(f"   Precio: ${producto['precio']} | Stock: {producto['stock']}")
    print(f"\nTotal de productos: {len(datos['productos'])}\n")

def listar_categorias():
    datos = cargar_productos()
    categorias = set(p["categoria"] for p in datos["productos"])
    print("\n--- Categorías disponibles ---")
    for cat in sorted(categorias):
        print(f"• {cat}")

def menu():
    while True:
        print("\n=== INVENTARIO DE PRODUCTOS ===")
        print("1. Listar todos los productos")
        print("2. Filtrar por categoría")
        print("3. Calcular valor total del inventario")
        print("4. Actualizar stock")
        print("5. Agregar producto")
        print("6. Ver categorías")
        print("7. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            listar_categorias()
            categoria = input("\nIngrese la categoría: ")
            filtrar_por_categoria(categoria)
        elif opcion == "3":
            calcular_valor_total()
        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            stock = int(input("Nuevo stock: "))
            actualizar_stock(nombre, stock)
        elif opcion == "5":
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            agregar_producto(nombre, categoria, precio, stock)
        elif opcion == "6":
            listar_categorias()
        elif opcion == "7":
            inicializar_productos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
