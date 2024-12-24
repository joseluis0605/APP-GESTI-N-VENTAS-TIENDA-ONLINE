import Cliente
import SQLiteDataAccessObject
from Producto import Producto
from Venta import  Venta
from Cliente import Cliente


def mostrar_info_gestion():
    print("\nGestionar Productos / Clientes / Ventas:")
    print("=========================================")
    print("1- Añadir nuevo Cliente")
    print("2- Añadir nuevo Producto")
    print("3- Añadir nueva Venta")
    print("4- Modificar Cliente")
    print("5- Modificar Producto")
    print("6- Consultar info Cliente")
    print("7- Consultar info Producto")
    print("8- Consultar info Venta")
    print("9- Mostrar Tabla Cliente")
    print("10- Mostrar Tabla Productos")
    print("11- Consultar Tabla Venta")
    print("**********************************************")


def mostrar_info_general():
    print("\nElige una de las siguientes opciones:")
    print("=========================================")
    print("1- Gestionar Productos / Clientes / Ventas")
    print("2- Ver Información de las estadísticas")
    print("-1- Salir del programa")
    print("**********************************************")


def mostrar_info_estadisticas():
    print("\nVer Información de las Estadísticas:")
    print("=====================================")
    print("1- Productos más vendidos")
    print("2- Cliente con más compras realizadas")
    print("3- Clientes que nunca han comprado")
    print("4- Ingresos totales por ventas")
    print("**********************************************")


def menu(database):
    cliente = Cliente()
    producto = Producto()
    venta = Venta()
    while True:
        mostrar_info_general()

        try:
            # Elegir entre 1 o 2 (gestionar o consultar estadísticas) o -1 (salir)
            entrada = int(input("--> "))

            # Si queremos salir del programa
            if entrada == -1:
                print("\nSaliendo del programa... Hasta pronto!")
                exit(0)

            # Nos protegemos de una entrada incorrecta
            elif entrada < 1 or entrada > 2:
                raise ValueError("¡Error! Introduce un número válido (1 o 2)")

            # Si queremos hacer tareas de gestión --> 1
            elif entrada == 1:
                mostrar_info_gestion()

                try:
                    entrada = int(input("--> "))
                    if entrada < 1 or entrada > 11:
                        raise ValueError("¡Error! Introduce un número válido (1-11)")

                    if entrada == 1:
                        print("Añadir nuevo Cliente")
                        # Función que crea un nuevo cliente
                        cliente.crear_cliente(database)
                    elif entrada == 2:
                        print("Añadir nuevo Producto")
                        # Aquí iría la función para añadir un producto
                        producto.crear_producto(database)
                    elif entrada == 3:
                        print("Añadir nueva Venta")
                        # Aquí iría la función para añadir una venta
                        venta.crear_venta(database)
                    elif entrada == 4:
                        print("Modificar info Cliente")
                        # Función modificar informacion de cliente manteniendo el dni y cambiando el resto de campos
                        cliente.update_cliente(database)
                    elif entrada == 5:
                        print("Modificar info Producto")
                        # Aquí iría la función para modificar un producto
                        producto.update_producto(database)
                    elif entrada == 6:
                        print("Consultar info Cliente")
                        # Función consultar informacion de cliente dado un DNI
                        cliente.mostrar_info_cliente(database)
                    elif entrada == 7:
                        print("Consultar info Producto")
                        # Aquí iría la función para consultar información de un producto
                        producto.mostrar_info_producto(database)
                    elif entrada == 8:
                        print("Consultar info Venta")
                        # Aquí iría la función para consultar información de una venta
                        venta.mostrar_info_venta(database)
                    elif entrada == 9:
                        print("Mostrar Tabla Cliente")
                        cliente.mostrar_tabla(database)
                    elif entrada == 10:
                        print("10- Mostrar Tabla Producto")
                        producto.mostrar_tabla(database)
                    elif entrada == 11:
                        print("11- Consultar Tabla Venta")
                        venta.mostrar_tabla(database)

                except ValueError:
                    print("¡Error! El número está fuera de rango (1-11)")
                continue

            # Si has elegido la opción de mostrar estadísticas --> 2
            elif entrada == 2:
                mostrar_info_estadisticas()

                try:
                    entrada = int(input("--> "))

                    # Nos protegemos de la entrada
                    if entrada < 1 or entrada > 4:
                        raise ValueError("¡Error! Introduce un número válido (1-4)")

                    elif entrada == 1:
                        print("Productos más vendidos")
                        # Aquí iría la función para obtener productos más vendidos
                        database.productos_mas_vendidos()
                    elif entrada == 2:
                        print("Cliente con más compras realizadas")
                        # Aquí iría la función para obtener el cliente con más compras
                        database.clientes_con_mas_compras()
                    elif entrada == 3:
                        print("Clientes que nunca han comprado")
                        # Aquí iría la función para obtener clientes que nunca han comprado
                        database.clientes_sin_compras()
                    elif entrada == 4:
                        print("Ingresos totales por ventas")
                        # Aquí iría la función para obtener ingresos totales por ventas
                        database.ingresos_totales()

                except ValueError:
                    print("¡Error! Número fuera de rango (1-4)")
                finally:
                    continue

        except ValueError:
            print("¡Error! El número está fuera de rango")