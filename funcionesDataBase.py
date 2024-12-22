"""
Módulo: funcionesDataBase.py
Descripción: Este módulo gestiona las interacciones con la base de datos.
Contiene funciones para insertar, actualizar, eliminar y consultar productos en la base de datos.
También incluye la función que valida si un producto ya existe antes de insertarlo, evitando duplicados en el sistema.
Las consultas a la base de datos están estructuradas para recuperar y manipular productos de manera eficiente.
"""

# Importamos los módulos necesarios.
import sqlite3
import os

# Ruta de la base de datos (formato multiplataforma).
DB_PATH = os.path.join(os.getcwd(), "inventario.db")

#---------------------------------------------------------------------------------------------------------------------
def db_crear_tabla_productos():
    """
    Crea la tabla 'productos' en la base de datos SQLite.
    Si la tabla ya existe, no se vuelve a crear.

    Estructura de la tabla:
        - id: Clave primaria autoincremental.
        - nombre: Nombre del producto (TEXT, NOT NULL).
        - descripcion: Descripción opcional del producto (TEXT).
        - categoria: Categoría del producto (TEXT, NOT NULL).
        - cantidad: Cantidad disponible (INTEGER, NOT NULL).
        - precio: Precio del producto (REAL, NOT NULL).
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conexion.commit()
        print("Tabla 'productos' creada o ya existente.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla 'productos': {e}")
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_producto_existe(nombre):
    """
    Verifica si un producto con el nombre dado ya existe en la tabla 'productos'.

    Args:
        nombre (str): Nombre del producto a verificar.

    Returns:
        bool: True si el producto existe, False en caso contrario.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        query = "SELECT COUNT(*) FROM productos WHERE nombre = ?"
        cursor.execute(query, (nombre,))
        count = cursor.fetchone()[0]
        return count > 0
    except sqlite3.Error as e:
        print(f"Error al verificar si el producto existe: {e}")
        return False
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_insertar_producto(producto):
    """
    Inserta un producto en la tabla 'productos'.
    Si el nombre del producto ya existe, no realiza la inserción.

    Args:
        producto (dict): Diccionario con las claves correspondientes a los campos:
            - nombre (str): Nombre del producto.
            - descripcion (str): Descripción opcional del producto.
            - categoria (str): Categoría del producto.
            - cantidad (int): Cantidad disponible.
            - precio (float): Precio del producto.

    Returns:
        str: Mensaje indicando el resultado de la operación.
    """
    conexion = None
    try:
        nombre = producto.get("nombre")
        if db_producto_existe(nombre):
            return f"Error: El producto '{nombre}' ya existe en la base de datos."

        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()

        query = """
            INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio)
            VALUES (?, ?, ?, ?, ?)
        """
        placeholders = (
            nombre,
            producto.get("descripcion"),
            producto.get("categoria"),
            producto.get("cantidad"),
            producto.get("precio"),
        )

        cursor.execute(query, placeholders)
        conexion.commit()
        return f"Producto '{nombre}' insertado correctamente."
    except sqlite3.Error as e:
        return f"Error al insertar el producto: {e}"
    except KeyError as e:
        return f"Falta clave requerida en el diccionario: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_get_productos():
    """
    Obtiene todos los productos de la tabla 'productos'.

    Returns:
        list: Lista de tuplas con los datos de los productos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as e:
        print(f"Error al obtener los productos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_get_producto_by_id(producto_id):
    """
    Obtiene un producto por su ID.

    Args:
        producto_id (int): ID del producto.

    Returns:
        tuple: Tupla con los datos del producto o None si no existe.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al obtener el producto por ID: {e}")
        return None
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_actualizar_producto(producto_id, nueva_cantidad):
    """
    Actualiza la cantidad de un producto.

    Args:
        producto_id (int): ID del producto.
        nueva_cantidad (int): Nueva cantidad del producto.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, producto_id))
        conexion.commit()
        print(f"Producto con ID {producto_id} actualizado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_eliminar_producto(producto_id):
    """
    Elimina un producto por su ID.

    Args:
        producto_id (int): ID del producto a eliminar.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conexion.commit()
        print(f"Producto con ID {producto_id} eliminado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        if conexion:
            conexion.close()


#---------------------------------------------------------------------------------------------------------------------
def db_get_productos_by_condicion(minimo_stock):
    """
    Obtiene los productos cuya cantidad es menor al stock mínimo.

    Args:
        minimo_stock (int): Cantidad mínima de stock.

    Returns:
        list: Lista de tuplas con los productos que cumplen la condición.
    """
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (minimo_stock,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener productos con bajo stock: {e}")
        return []
    finally:
        if conexion:
            conexion.close()