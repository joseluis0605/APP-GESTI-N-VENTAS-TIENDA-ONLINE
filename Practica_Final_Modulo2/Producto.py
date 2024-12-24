import Entradas_Database.ListadoProductos

class Producto:

    def __init__(self):
        self.id_producto = ""
        self.nombre = ""
        self.precio = -1

    def crear_producto(self, database):
        nombre = str(input("Introduce el nombre del producto: "))
        precio = float(input("Introduce el precio del producto: "))
        database.insertar_producto(nombre, precio)

    def update_producto(self, database):
        id_producto = str(input("Introduce el id del producto: "))
        nombre = str(input("Introduce el nombre: "))
        precio = float(input("Introduce el precio del producto: "))
        database.actualizar_producto(id_producto, nombre, precio)

    def mostrar_info_producto(self, database):
        id_producto = str(input("Introduce el id del producto: "))
        database.mostrar_info_producto(id_producto)

    def mostrar_tabla(self, database):
        database.mostrar_tabla_producto()




###############################################################################################
##### Esto es para rellenar la base de datos con contenido
    def insertar_monton(self, database):
        # se insertarán usuarios creador al azar para llenar la base de datos
        listado_productos= Entradas_Database.ListadoProductos.get_listado_productos()

        for producto in listado_productos:
            nombre, precio = producto
            database.insertar_producto(nombre, precio)