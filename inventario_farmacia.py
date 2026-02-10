# Inventario de Farmacia
# Programación Básica - Práctica POO

inventario = {}
total_ventas = 0.0

def registrar_medicamento():
    nombre = input("Nombre del medicamento: ").lower()
    if nombre in inventario:
        print("⚠️ El medicamento ya existe.")
        return

    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del medicamento: "))

    inventario[nombre] = {
        "cantidad": cantidad,
        "precio": precio
    }
    print("✅ Medicamento registrado correctamente.")

def consultar_inventario():
    if not inventario:
        print("📦 Inventario vacío.")
        return

    print("\n--- INVENTARIO ---")
    for nombre, datos in inventario.items():
        print(f"Medicamento: {nombre}")
        print(f"Cantidad: {datos['cantidad']}")
        print(f"Precio: RD${datos['precio']}")
        print("------------------")

def vender_medicamento():
    global total_ventas
    nombre = input("Medicamento a vender: ").lower()

    if nombre not in inventario:
        print("❌ Medicamento no existe.")
        return

    cantidad_vender = int(input("Cantidad a vender: "))

    if cantidad_vender > inventario[nombre]["cantidad"]:
        print("⚠️ Stock insuficiente.")
        return

    inventario[nombre]["cantidad"] -= cantidad_vender
    venta = cantidad_vender * inventario[nombre]["precio"]
    total_ventas += venta

    print(f"✅ Venta realizada. Total: RD${venta}")

def mostrar_total_ventas():
    print(f"\n💰 Total de ventas del día: RD${total_ventas}")

def menu():
    print("""
--- MENÚ FARMACIA ---
1. Registrar medicamento
2. Consultar inventario
3. Vender medicamento
4. Mostrar total de ventas
5. Salir
""")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_medicamento()
    elif opcion == "2":
        consultar_inventario()
    elif opcion == "3":
        vender_medicamento()
    elif opcion == "4":
        mostrar_total_ventas()
    elif opcion == "5":
        print("👋 Saliendo del sistema...")
        break
    else:
        print("❌ Opción inválida.")
