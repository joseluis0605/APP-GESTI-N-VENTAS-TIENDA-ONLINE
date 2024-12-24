import sqlite3
from sqlite3 import Cursor


class SQLiteDataAccessObject:

    nombre = "database.db"

    # crear base de datos con el nombre
    def crear_database(self):
        conexion = sqlite3.connect(self.nombre)
        conexion.close()

    def crear_tabla(self):
        conexion = sqlite3.connect(self.nombre)
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE CLIENTE (
                ID VARCHAR(20)  PRIMARY KEY,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                TELEFONO INTEGER
        )''')

        cursor.execute('''CREATE TABLE PRODUCTO (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PRECIO FLOAT           
        )''')

        cursor.execute('''CREATE TABLE VENTA(
                ID_CLIENTE VARCHAR(20),
                ID_PRODUCTO INTEGER
        )''')

        conexion.commit()
        cursor.close()
        conexion.close()

    ####################################
    ### OPERACIONES CON EL CLIENTE
    ####################################

    def insertar_cliente(self, ID, NOMBRE, APELLIDO, TELEFONO):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            id_cliente= str(ID)
            nombre_cliente = str(NOMBRE)
            apellido_cliente = str(APELLIDO)
            telefono_cliente = int(TELEFONO)

            cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (id_cliente,))
            resultado = cursor.fetchone()
            if resultado:
                print("El cliente ya exite")
            else:
                cursor.execute("INSERT INTO CLIENTE (ID, NOMBRE, APELLIDO, TELEFONO) VALUES (?, ?, ?, ?)",
                    (id_cliente, nombre_cliente, apellido_cliente, telefono_cliente))

            conexion.commit()
            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    def actualizar_cliente(self, ID, NOMBRE, APELLIDO, TELEFONO):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (ID,))
            resultado = cursor.fetchone()

            # si existe resultado, actualizamos
            if resultado:
                cursor.execute("""
                            UPDATE CLIENTE
                            SET NOMBRE = ?, APELLIDO = ?, TELEFONO = ?
                            WHERE ID = ?;
                        """, (NOMBRE, APELLIDO, TELEFONO, ID))
            else:  # si no, lo creamos de nuevo
                print("El cliente no existe")

            conexion.commit()
            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    def mostrar_info_cliente(self, ID: str):
        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            dni= str(ID)
            cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (dni,))
            resultado = cursor.fetchone()
            if resultado:
                dni, nombre, apellido, telefono = resultado
                print(f"dni: {dni}, nombre: {nombre}, apellido: {apellido}, telefono: {telefono}")
            else:
                print("El cliente no existe")

            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)


    def mostrar_tabla_cliente(self):
        conexion = sqlite3.connect(self.nombre)
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CLIENTE")
        resultado = cursor.fetchall()
        if resultado:
            for row in resultado:
                dni, nombre, apellido, telefono = row
                print(f"dni: {dni}, nombre: {nombre}, apellido: {apellido}, telefono: {telefono}")
        else:
            print("La tabla se encuentra vacia")

        cursor.close()
        conexion.close()





    ####################################
    ### OPERACIONES CON EL PRODUCTO
    ####################################

    def insertar_producto(self, NOMBRE, PRECIO):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            nombre_producto = str(NOMBRE)
            precio_producto = float(PRECIO)

            cursor.execute("SELECT * FROM PRODUCTO WHERE NOMBRE = ?", (nombre_producto,))

            resultado = cursor.fetchone()
            if resultado:
                print("El producto ya existe")
            else:
                cursor.execute("INSERT INTO PRODUCTO (NOMBRE, PRECIO) VALUES (?, ?)",(nombre_producto,precio_producto))
                conexion.commit()

            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    def actualizar_producto(self, ID, NOMBRE, PRECIO):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM PRODUCTO WHERE ID = ?", (ID,))
            resultado = cursor.fetchone()

            # si existe resultado, actualizamos
            if resultado:
                cursor.execute("""
                            UPDATE PRODUCTO
                            SET NOMBRE = ?, PRECIO = ?
                            WHERE ID = ?;
                        """, (NOMBRE, PRECIO, ID,))
            else:  # si no, lo creamos de nuevo
                print("El producto no existe")

            conexion.commit()
            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    def mostrar_info_producto(self, ID: int):
        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            id_producto= int(ID)
            cursor.execute("SELECT * FROM PRODUCTO WHERE ID = ?", (id_producto,))
            resultado = cursor.fetchone()
            if resultado:
                id_producto, nombre, precio = resultado
                print(f"id_producto: {id_producto}, nombre: {nombre}, precio: {precio}€")
            else:
                print("El producto no existe")

            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    def mostrar_tabla_producto(self):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM PRODUCTO")
            resultado = cursor.fetchall()
            if resultado:
                for row in resultado:
                    id_producto, nombre, precio = row
                    print(f"id_producto: {id_producto}, nombre: {nombre}, precio: {precio}€")
            else:
                print("La tabla se encuentra vacia")

        except sqlite3.Error as error:
            print(error)

    ####################################
    ### OPERACIONES CON LAS VENTAS
    ####################################


    def insertar_venta(self, ID_CLIENTE, ID_PRODUCTO):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            id_cliente = str(ID_CLIENTE)
            id_producto = int(ID_PRODUCTO)

            cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (id_cliente,))
            existe_cliente = cursor.fetchone()

            cursor.execute("SELECT * FROM PRODUCTO WHERE ID = ?", (id_producto,))
            existe_producto = cursor.fetchone()

            if existe_cliente and existe_producto:
                cursor.execute("INSERT INTO VENTA (ID_CLIENTE, ID_PRODUCTO) VALUES (?, ?)",(id_cliente,id_producto))
                conexion.commit()

            else:
                print("El producto o el cliente no existe")

            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(error)

    # muestra las compras de un cliente
    def mostrar_info_venta_cliente(self, ID_CLIENTE):
        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            # Consulta las ventas asociadas al cliente
            cursor.execute("SELECT * FROM VENTA WHERE ID_CLIENTE = ?", (ID_CLIENTE,))
            ventas = cursor.fetchall()  # Lista de todas las ventas de ese cliente

            if ventas:
                for venta in ventas:
                    id_producto = venta[1]  # Supongamos que columna 1 tiene el ID del producto

                    # Obtén información del cliente
                    cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (ID_CLIENTE,))
                    cliente = cursor.fetchone()  # Solo un cliente esperado
                    if cliente:
                        dni_cliente, nombre_cliente, apellido_cliente, telefono_cliente = cliente
                        print(f"Cliente: {nombre_cliente} {apellido_cliente}, DNI: {dni_cliente}")

                    # Obtén información del producto
                    cursor.execute("SELECT * FROM PRODUCTO WHERE ID = ?", (id_producto,))
                    producto = cursor.fetchone()
                    if producto:
                        id_producto, nombre_producto, precio_producto = producto
                        print(f"Producto vendido: {nombre_producto}, Precio: {precio_producto}")

                    print("-" * 40)
            else:
                print("No hay ventas para ese cliente.")

            cursor.close()
            conexion.close()

        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")

    def mostrar_tabla_venta(self):
        try:
            # Conexión a la base de datos
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()

            # Consulta todos los registros de la tabla VENTA
            cursor.execute("SELECT * FROM VENTA")
            ventas = cursor.fetchall()

            if ventas:
                for venta in ventas:
                    id_cliente, id_producto = venta

                    # Obtener información del cliente
                    cursor.execute("SELECT * FROM CLIENTE WHERE ID = ?", (id_cliente,))
                    info_cliente = cursor.fetchone()

                    if info_cliente:
                        dni, nombre_cliente, apellido, telefono = info_cliente
                        print(f"Cliente:")
                        print(f"  - DNI: {dni}")
                        print(f"  - Nombre: {nombre_cliente} {apellido}")
                        print(f"  - Teléfono: {telefono}")
                    else:
                        print(f"Cliente con ID {id_cliente} no encontrado.")

                    # Obtener información del producto
                    cursor.execute("SELECT * FROM PRODUCTO WHERE ID = ?", (id_producto,))
                    info_producto = cursor.fetchone()

                    if info_producto:
                        id_producto, nombre_producto, precio_producto = info_producto
                        print(f"Producto:")
                        print(f"  - ID Producto: {id_producto}")
                        print(f"  - Nombre: {nombre_producto}")
                        print(f"  - Precio: {precio_producto} €")
                    else:
                        print(f"Producto con ID {id_producto} no encontrado.")

                    print("-" * 40)  # Separador visual entre registros

            else:
                print("La tabla VENTA se encuentra vacía.")

        except sqlite3.Error as error:
            print(f"Error al acceder a la base de datos: {error}")

    ####################################
    ### OPERACIONES CON LAS ESTADISTICAS
    ####################################
    def productos_mas_vendidos(self):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.NOMBRE, COUNT(v.ID_PRODUCTO) AS TOTAL_VENTAS
                FROM VENTA v
                JOIN PRODUCTO p ON v.ID_PRODUCTO = p.ID
                GROUP BY p.ID
                ORDER BY TOTAL_VENTAS DESC;
            """)
            resultado = cursor.fetchall()
            print("Productos más vendidos:")
            for row in resultado:
                print(f"Producto: {row[0]}, Ventas: {row[1]}")
            cursor.close()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al obtener productos más vendidos:", e)

    def clientes_con_mas_compras(self):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT c.nombre, c.apellido, COUNT(v.id_cliente) AS total_compras
                FROM VENTA v
                JOIN CLIENTE c ON v.id_cliente = c.id
                GROUP BY c.id
                ORDER BY total_compras DESC;
            """)
            resultado = cursor.fetchall()
            print("Clientes con mayor número de compras:")
            for row in resultado:
                print(f"Cliente: {row[0]} {row[1]}, Compras: {row[2]}")
            cursor.close()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al obtener clientes con más compras:", e)

    def clientes_sin_compras(self):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT c.nombre, c.apellido
                FROM CLIENTE c
                LEFT JOIN VENTA v ON c.id = v.id_cliente
                WHERE v.id_cliente IS NULL;
            """)
            resultado = cursor.fetchall()
            print("Clientes sin compras:")
            for row in resultado:
                print(f"Cliente: {row[0]} {row[1]}")
            cursor.close()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al obtener clientes sin compras:", e)

    def ingresos_totales(self):

        try:
            conexion = sqlite3.connect(self.nombre)
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT SUM(p.precio) AS ingresos_totales
                FROM VENTA v
                JOIN PRODUCTO p ON v.id_producto = p.id;
            """)
            resultado = cursor.fetchone()
            print(f"Ingresos totales por ventas: {resultado[0]} €")
            cursor.close()
            conexion.close()
        except sqlite3.Error as e:
            print("Error al calcular ingresos totales:", e)