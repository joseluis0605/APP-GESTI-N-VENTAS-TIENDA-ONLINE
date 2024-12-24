import Entradas_Database.ListadoClientes

class Cliente:

    def __init__(self):
        self.id_cliente = ""
        self.nombre = ""
        self.apellido = ""
        self.telefono = 0

    def crear_cliente(self, database):
        self.id_cliente = str(input("Introduce el dni: "))
        self.nombre = str(input("Introduce el nombre: "))
        self.apellido = str(input("Introduce el apellido: "))
        self.telefono = int(input("Introduce el telefono: "))
        database.insertar_cliente(self.id_cliente, self.nombre, self.apellido, self.telefono)

    def update_cliente(self, database):
        id_cliente = str(input("Introduce el dni: "))
        nombre = str(input("Introduce el nombre: "))
        apellido = str(input("Introduce el apellido: "))
        telefono = int(input("Introduce el telefono: "))
        database.actualizar_cliente(id_cliente, nombre, apellido, telefono)

    def mostrar_info_cliente(self, database):
        id_cliente = str(input("Introduce el dni: "))
        database.mostrar_info_cliente(id_cliente)

    def mostrar_tabla(self, database):
        database.mostrar_tabla_cliente()




###############################################################################################
##### Esto es para rellenar la base de datos con contenido
    def insertar_monton(self, database):
        # se insertarán usuarios creador al azar para llenar la base de datos
        listado_clientes= Entradas_Database.ListadoClientes.get_listado_clientes()

        for cliente in listado_clientes:
            dni, nombre, apellido, telefono = cliente
            database.insertar_cliente(dni, nombre, apellido, telefono)