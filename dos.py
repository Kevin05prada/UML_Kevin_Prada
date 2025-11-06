print("Bienvenido a la Biblioteca Virtual")
print( )

print("MENÚ")
print("1. Consultar libros")
print("2. Prestar libros")
print("3. Devolver libros")
print("4. Salir")

opc = 0
opc = int(input("Seleccione una opción: "))
print( )
while opc != 4:
    match opc:
        case 1:
            print("lista de libros")
            print( )
            
            print("Libro de Superman")
            print("Libro de Cocodrilo")
            print("Libro de Peces")
            print("Libro de Perros")
            print("Libro de Animales")
            print("Libro de Princesas")
            print("Libro de Arboles")
            print("Libro de Paises")
            print("Libro de Comida")
            print("Libro de Maquinas")
             
        case 2:
            print("Libro prestados")
        case 3:
            print("Se devolvio libros")
        case _:
            print("Salio")    
    print( )
    opc = int(input("Seleccione la opción 2,3 o 4: "))
    print( )