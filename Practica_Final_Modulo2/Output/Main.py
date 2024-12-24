import Banner
from Cliente import Cliente
from Producto import Producto
from SQLiteDataAccessObject import SQLiteDataAccessObject
import Output.Menu
from Venta import Venta

if __name__ == '__main__':

    # inicializamos la base de datos
    database = SQLiteDataAccessObject()
    database.crear_database()
    Banner.presentacion()

    Output.Menu.menu(database)










