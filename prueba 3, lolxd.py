libros = []
ventas = []

def registrar_libro():
    print("---Registrar libro---")
    while True:
        titulo = input("Ingrese el título del libro: ").capitalize()
        if titulo == "":
            print("Error, ingrese algún dato")
        else:
            break
    while True:
        autor = input("Ingrese el nombre del autor: ").capitalize()
        if autor == "":
            print("Error, ingrese algún dato")
        else:
            break
    while True:
        genero = input("Ingrese el género del libro: ").capitalize()
        if genero == "":
            print("Error, ingrese algún dato")
        else:
            break
    while True:
        cantidad = int(input("Ingrese la cantidad de libros: "))
        if cantidad <= 0:
            print("Error, ingrese un número mayor que cero")
        else:
            break
    while True:
        precio = int(input("Ingrese el precio del libro: $"))
        if precio <= 0:
            print("Error, ingrese un número mayor que cero")
        else:
            break

    libros.append({"Titulo": titulo, "Autor": autor, "Genero": genero, "Cantidad": cantidad, "Precio": precio})

def listar_libros():
    print("---Lista de libros---")
    for i in libros:
        print(i)

def registrar_venta():
    print("---Registrar Venta---")
    titulo = input("Ingrese el título del libro: ").capitalize()
    for i in libros:
        if i["Titulo"] == titulo:
            while True:
                cantidad = int(input("Ingrese la cantidad vendida: "))
                if cantidad > i["Cantidad"]:
                    print("Error, no existe esa cantidad de ibros")
                elif cantidad <= 0:
                    print("Error, ingrese una cantidad válida")
                else:
                    i["Cantidad"] -= cantidad
                    ventas.append({"Titulo": titulo, "Cantidad": cantidad, "Precio": i["Precio"] * cantidad})
                    print("Se registrO exitosamente")
                    return
    print("Libro no encontrado")

def imprimir_reporte_ventas():
    print("---Reporte de Ventas---")
    if not ventas:
        print("No hay ventas registradas")
    else:
        for venta in ventas:
            print(venta)

def generar_txt_registro_ventas():
    print("---Generar Registro de Ventas en .TXT---")
    with open("registro_ventas.txt", "w") as archivo:
        for venta in ventas:
            archivo.write(f"{venta}\n")
    print("Se guardo el registro exitosamente")

while True:
    try:
        print("MENU")
        op = int(input("1. Registrar libro\n2. Listar todos los libros\n3. Registrar venta\n4. Imprimir reporte de ventas\n5. Generar txt\n6. Salir del Programa\nIngrese una opción: "))
        if op == 1:
            registrar_libro()
        elif op == 2:
            listar_libros()
        elif op == 3:
            registrar_venta()
        elif op == 4:
            imprimir_reporte_ventas()
        elif op == 5:
            generar_txt_registro_ventas()
        elif op == 6:
            print("Saliendo del sistema...")
            break
    except ValueError:
        print("Error, ingrese un número válido")