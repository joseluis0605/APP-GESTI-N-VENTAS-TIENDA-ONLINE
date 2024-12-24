import SQLiteDataAccessObject
import Entradas_Database.ListadoVentas
class Venta:

    def __init__(self):
        self.id_cliente = ""
        self.id_venta = 0

    def crear_venta(self, database):
        id_cliente = str(input("Introduce el dni del cliente: "))
        id_venta = int(input("Introduce el id del producto: "))
        database.insertar_venta(id_cliente, id_venta)

    def mostrar_info_venta(self, database):
        id_cliente = str(input("Introduce el dni del cliente: "))
        database.mostrar_info_venta_cliente(id_cliente)

    def mostrar_tabla(self, database):
        database.mostrar_tabla_venta()

###############################################################################################
##### Esto es para rellenar la base de datos con contenido
    def insertar_monton(self, database):
        # se insertarán usuarios creador al azar para llenar la base de datos
        listado_ventas= Entradas_Database.ListadoVentas.get_listado_ventas()

        for venta in listado_ventas:
            id_cliente, id_producto = venta
            database.insertar_venta(id_cliente, id_producto)