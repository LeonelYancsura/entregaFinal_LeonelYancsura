"""
Módulo: funcionesValidacion.py
Descripción: Este módulo contiene funciones para validar datos ingresados por el usuario.
Incluye validaciones para asegurar que los datos como el nombre, descripción, categoría, cantidad y precio sean correctos y estén en el formato adecuado.
Además, incluye una opción para verificar si un producto ya existe en la base de datos antes de permitir su inserción.
"""

from funcionesDataBase import db_producto_existe  # Importa función para verificar existencia.

#---------------------------------------------------------------------------------------------------------------------
def validacion_get_nombre(verificar_existencia=False):
    """
    Solicita al usuario que ingrese el nombre del producto.
    - No se admite dato nulo.
    - El nombre puede contener cualquier caracter.
    - Opcionalmente, verifica si el nombre ya existe en la base de datos.

    Args:
        verificar_existencia (bool): Si es True, verifica si el producto ya existe en la base de datos.

    Returns:
        str: Nombre del producto validado.
    """
    while True:
        try:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Error: No se admite dato nulo. Por favor, ingrese un nombre.")
                continue

            if verificar_existencia:
                if db_producto_existe(nombre):
                    print(f"Error: El producto '{nombre}' ya existe. Ingrese otro nombre.")
                    continue

            return nombre
        except Exception as e:
            print(f"Error inesperado: {e}")


#---------------------------------------------------------------------------------------------------------------------
def validacion_get_descripcion():
    """
    Solicita al usuario que ingrese la descripción del producto.
    - Se admite dato nulo.
    - La descripción puede contener cualquier caracter.

    Returns:
        str: Descripción del producto.
    """
    try:
        descripcion = input("Descripción: ").strip()
        return descripcion
    except Exception as e:
        print(f"Error inesperado: {e}")
        return ""  # En caso de error, se retorna una cadena vacía.


#---------------------------------------------------------------------------------------------------------------------
def validacion_get_categoria():
    """
    Solicita al usuario que ingrese la categoría del producto.
    - No se admite dato nulo.
    - La categoría puede contener cualquier caracter.

    Returns:
        str: Categoría del producto validada.
    """
    while True:
        try:
            categoria = input("Categoría: ").strip()
            if categoria:
                return categoria
            else:
                print("Error: No se admite dato nulo. Por favor, ingrese una categoría.")
        except Exception as e:
            print(f"Error inesperado: {e}")


#---------------------------------------------------------------------------------------------------------------------
def validacion_get_cantidad(mensaje="Cantidad: "):
    """
    Solicita al usuario que ingrese la cantidad del producto.
    - No se admite dato nulo.
    - La cantidad debe ser un número entero mayor a 0.

    Args:
        mensaje (str): Mensaje personalizado para solicitar la cantidad.

    Returns:
        int: Cantidad validada.
    """
    while True:
        try:
            cantidad = int(input(f"{mensaje} ").strip())
            if cantidad > 0:
                return cantidad
            else:
                print("Error: La cantidad debe ser un número entero mayor a 0.")
        except ValueError:
            print("Error: Tipo de dato no válido. Por favor, ingrese un número entero.")
        except Exception as e:
            print(f"Error inesperado: {e}")


#---------------------------------------------------------------------------------------------------------------------
def validacion_get_precio():
    """
    Solicita al usuario que ingrese el precio del producto.
    - No se admite dato nulo.
    - El precio debe ser un número entero o float mayor a 0.

    Returns:
        float: Precio validado.
    """
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if precio > 0:
                return precio
            else:
                print("Error: El precio debe ser un número mayor a 0.")
        except ValueError:
            print("Error: Tipo de dato no válido. Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

