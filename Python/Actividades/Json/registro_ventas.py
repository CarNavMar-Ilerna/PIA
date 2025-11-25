import json
import os

ARCHIVO_JSON = "registro_ventas.json"

def cargar_ventas():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    else:
        return {"ventas": []}

def guardar_ventas(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def inicializar_ventas():
    ventas_iniciales = {
        "ventas": [
            {"producto": "Laptop", "cantidad": 2, "precio": 1000, "fecha": "2024-10-28"},
            {"producto": "Teclado", "cantidad": 5, "precio": 50, "fecha": "2024-10-27"},
            {"producto": "Mouse", "cantidad": 10, "precio": 25, "fecha": "2024-10-28"},
            {"producto": "Monitor", "cantidad": 3, "precio": 300, "fecha": "2024-10-26"},
            {"producto": "Webcam", "cantidad": 4, "precio": 80, "fecha": "2024-10-29"},
            {"producto": "Auriculares", "cantidad": 8, "precio": 60, "fecha": "2024-10-28"},
            {"producto": "Tablet", "cantidad": 2, "precio": 500, "fecha": "2024-10-30"},
            {"producto": "Impresora", "cantidad": 1, "precio": 200, "fecha": "2024-10-27"},
            {"producto": "Disco Duro", "cantidad": 6, "precio": 100, "fecha": "2024-10-29"},
            {"producto": "Memoria USB", "cantidad": 15, "precio": 15, "fecha": "2024-10-28"}
        ]
    }
    guardar_ventas(ventas_iniciales)
    print("✓ Registro inicializado con 10 ventas")

def calcular_total_ventas():
    datos = cargar_ventas()
    total = sum(v["cantidad"] * v["precio"] for v in datos["ventas"])
    print(f"\n💰 Total de ventas: ${total:,.2f}")
    return total

def filtrar_por_fecha(fecha):
    datos = cargar_ventas()
    ventas_filtradas = [v for v in datos["ventas"] if v["fecha"] == fecha]
    
    if ventas_filtradas:
        print(f"\n--- Ventas del {fecha} ---")
        total_dia = 0
        for venta in ventas_filtradas:
            subtotal = venta["cantidad"] * venta["precio"]
            total_dia += subtotal
            print(f"• {venta['producto']}: {venta['cantidad']} x ${venta['precio']} = ${subtotal}")
        print(f"\nTotal del día: ${total_dia:,.2f}")
    else:
        print(f"No se encontraron ventas para la fecha {fecha}")
    
    return ventas_filtradas

def filtrar_por_producto(producto):
    datos = cargar_ventas()
    ventas_filtradas = [v for v in datos["ventas"] if producto.lower() in v["producto"].lower()]
    
    if ventas_filtradas:
        print(f"\n--- Ventas de '{producto}' ---")
        total_producto = 0
        cantidad_total = 0
        for venta in ventas_filtradas:
            subtotal = venta["cantidad"] * venta["precio"]
            total_producto += subtotal
            cantidad_total += venta["cantidad"]
            print(f"• Fecha: {venta['fecha']} - Cantidad: {venta['cantidad']} - Subtotal: ${subtotal}")
        print(f"\nCantidad total vendida: {cantidad_total}")
        print(f"Total en ventas: ${total_producto:,.2f}")
    else:
        print(f"No se encontraron ventas del producto '{producto}'")
    
    return ventas_filtradas

def agregar_venta(producto, cantidad, precio, fecha):
    datos = cargar_ventas()
    nueva_venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "fecha": fecha
    }
    datos["ventas"].append(nueva_venta)
    guardar_ventas(datos)
    subtotal = cantidad * precio
    print(f"✓ Venta agregada: {cantidad} x {producto} = ${subtotal}")

def listar_ventas():
    datos = cargar_ventas()
    print("\n--- REGISTRO DE VENTAS ---")
    for i, venta in enumerate(datos["ventas"], 1):
        subtotal = venta["cantidad"] * venta["precio"]
        print(f"{i}. {venta['producto']} - {venta['cantidad']} unidades")
        print(f"   Precio: ${venta['precio']} | Subtotal: ${subtotal} | Fecha: {venta['fecha']}")
    print(f"\nTotal de ventas registradas: {len(datos['ventas'])}\n")

def menu():
    while True:
        print("\n=== REGISTRO DE VENTAS ===")
        print("1. Listar todas las ventas")
        print("2. Calcular total de ventas")
        print("3. Filtrar por fecha")
        print("4. Filtrar por producto")
        print("5. Agregar nueva venta")
        print("6. Inicializar con datos de ejemplo")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            listar_ventas()
        elif opcion == "2":
            calcular_total_ventas()
        elif opcion == "3":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            filtrar_por_fecha(fecha)
        elif opcion == "4":
            producto = input("Ingrese el nombre del producto: ")
            filtrar_por_producto(producto)
        elif opcion == "5":
            producto = input("Producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            agregar_venta(producto, cantidad, precio, fecha)
        elif opcion == "6":
            inicializar_ventas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
