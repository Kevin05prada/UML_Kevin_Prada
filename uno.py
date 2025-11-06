libros = {
    "1001": {"titulo": "Python Básico", "disponible": True},
    "1002": {"titulo": "Introducción a UML", "disponible": True},
    "1003": {"titulo": "Diseño de Software", "disponible": True},
    "1004": {"titulo": "Base de Datos", "disponible": True}
}

# Lista donde se guardan los libros que el usuario lleva
prestados_usuario = []

print("Bienvenido a la Biblioteca Virtual")

opcion = 0

while opcion != 4:
    print("\n------- MENÚ -------")
    print("1. Consultar libros")
    print("2. Prestar libros")
    print("3. Devolver libros")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        # --------------------------------------------------------
        case 1:  # Consultar libros
            print("\n LISTA DE LIBROS DISPONIBLES:")
            for codigo, datos in libros.items():
                estado = "Disponible " if datos["disponible"] else "Prestado "
                print(f"{codigo}: {datos['titulo']} → {estado}")

        # --------------------------------------------------------
        case 2:  # Prestar libros
            cantidad = int(input("\n¿Cuántos libros desea llevar?: "))

            for i in range(cantidad):
                codigo = input(f"Ingrese código del libro #{i+1}: ")

                if codigo in libros:
                    if libros[codigo]["disponible"]:
                        libros[codigo]["disponible"] = False
                        prestados_usuario.append(codigo)
                        print(f"Prestado: {libros[codigo]['titulo']}")
                    else:
                        print("Ese libro ya está prestado.")
                else:
                    print("Código incorrecto.")

            print(f"\n Libros que llevas ahora: {len(prestados_usuario)}")

        # --------------------------------------------------------
        case 3:  # Devolver libros
            if len(prestados_usuario) == 0:
                print("No tienes libros para devolver.")
                continue

            print("\nTus libros prestados:")
            for codigo in prestados_usuario:
                print(f"- {codigo}: {libros[codigo]['titulo']}")

            print("\n1. Devolver un libro")
            print("2. Devolver todos")

            opcion_devolver = int(input("Seleccione: "))

            # Devolver uno
            if opcion_devolver == 1:
                cod = input("Ingrese el código a devolver: ")
                if cod in prestados_usuario:
                    prestados_usuario.remove(cod)
                    libros[cod]["disponible"] = True
                    print(f"Has devuelto: {libros[cod]['titulo']}")
                else:
                    print("No tienes ese libro prestado.")

            # Devolver todos
            elif opcion_devolver == 2:
                for cod in prestados_usuario:
                    libros[cod]["disponible"] = True
                prestados_usuario.clear()
                print("Has devuelto todos los libros.")

            else:
                print("Opción no válida.")

        # --------------------------------------------------------
        case 4:
            print("Saliendo de la Biblioteca Virtual...")

        case _:
            print("Opción no válida.")