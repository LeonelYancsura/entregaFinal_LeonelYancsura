"""
Módulo: funcionesMenu.py
Descripción: Este módulo contiene las funciones relacionadas con el menú interactivo que se presenta al usuario.
Gestiona la visualización de opciones y la ejecución de las tareas relacionadas, como registrar, mostrar, actualizar y eliminar productos.
Cada opción del menú se vincula con una función que interactúa con la base de datos para manipular los productos.
"""

from funcionesDataBase import *
from funcionesValidacion import *
from colorama import Fore

#---------------------------------------------------------------------------------------------------------------------
def menu_mostrar_opciones():
    """
    menu_mostrar_opciones()
    1. muestra en consola las opciones disponibles
    2. captura y retorna la opcion seleccionada
    """
    print(Fore.CYAN + "-" * 30)
    print(Fore.GREEN + " Menu principal ")
    print(Fore.CYAN + "-" * 30)
    print(Fore.YELLOW + """
           1. Agregar producto.
           2. Mostrar productos.
           3. Actualizar inventario.
           4. Eliminar producto.
           5. Buscar producto.
           6. Reporte de bajo stock.
           7. Salir.
       """)
    opcion = input(Fore.MAGENTA + "Seleccion una opción: ")
    #Agregar un modulo de validacion para evitar errores - PENDIENTE
    #Retorna un STR
    return opcion


#---------------------------------------------------------------------------------------------------------------------
def menu_registrar_producto():
    """
    menu_registrar_producto()
    1. captura todos los datos
    2. valida los datos y los almacena en un diccionario
    3. llama a db_insertar_producto(producto) y le pasa el diccionario producto para que lo inserte en la base de datos
    """
    print(Fore.CYAN + "\nIngrese los siguientes datos del producto: ")
    nombre = validacion_get_nombre()

    # Validar si el producto ya existe en la base de datos
    if db_producto_existe(nombre):
        print(Fore.RED + f"ERROR: Ya existe un producto con el nombre '{nombre}'.")
        return  # Finaliza la ejecución si el producto ya existe

    descripcion = validacion_get_descripcion()
    categoria = validacion_get_categoria()
    cantidad = validacion_get_cantidad()
    precio = validacion_get_precio()

    #Creamos un diccionario temporal
    producto={
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insertar_producto(producto)
    print(Fore.GREEN + "\nProducto insertado exitosamente")


#---------------------------------------------------------------------------------------------------------------------
def menu_mostrar_productos():
    """
    menu_mostrar_productos()
    1. no recibe ningún argumento
    2. llama a db_get_productos() que retorna una lista de tuplas con el contenido de la tabla
    3. usamos un bucle for para mostrar en consola
    """
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print(Fore.RED + "No hay productos que mostrar")


#---------------------------------------------------------------------------------------------------------------------
def menu_actualizar_producto():
    """
    menu_actualizar_producto()
    1. solicita al usuario que ingrese el id del producto a modificar
    2. buscamos el producto en la tabla (si no existe informamos)
    3. mostramos cantidad actual y pedimos que ingrese la nueva cantidad
    4. llamar a db_actualizar_registro(id, nueva_cantidad)
    """
    producto_id = int(input(Fore.MAGENTA + "\nIngrese el id del producto a actualizar: "))
    get_producto = db_get_producto_by_id(producto_id)
    if not get_producto:
        print(Fore.RED + "ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(Fore.YELLOW + f"Cantidad actual {get_producto[4]} ")
        nueva_cantidad = validacion_get_cantidad("Nueva cantidad: ")
        db_actualizar_producto(producto_id, nueva_cantidad)
        print(Fore.GREEN + "Registro actualizado exitosamente!")


#---------------------------------------------------------------------------------------------------------------------
def menu_eliminar_producto():
    """
    menu_eliminar_producto()
    1. solicita al usuario que ingrese el id del producto a eliminar
    2. buscamos el producto en la tabla (si no existe informamos)
    3. mostramos el producto y solicitamos confirmación
    4. llamar a db_eliminar_producto(id)
    """
    producto_id = int(input(Fore.MAGENTA + "\nIngrese el id del producto a eliminar: "))
    get_producto = db_get_producto_by_id(producto_id)
    if not get_producto:
        print(Fore.RED + "ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(Fore.YELLOW + "\nATENCION: se eliminará el siguiente registro:")
        print(Fore.YELLOW + str(get_producto))
        confirmacion = input(Fore.CYAN + "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(producto_id)
            print(Fore.GREEN + "Registro eliminado exitosamente!")
        else:
            print(Fore.RED + "Operación cancelada.")


#---------------------------------------------------------------------------------------------------------------------
def menu_buscar_producto():
    """
    menu_buscar_producto()
    1. solicita al usuario que ingrese el id del producto a buscar
    2. llamar a db_get_producto_by_id(id)
    """
    producto_id = int(input(Fore.MAGENTA + "\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(producto_id)
    if not get_producto:
        print(Fore.RED + "ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(Fore.GREEN + str(get_producto))


#---------------------------------------------------------------------------------------------------------------------
def menu_reporte_bajo_stock():
    """
    menu_reporte_bajo_stock()
    1. solicita al usuario que ingrese la cantidad mínima para el reporte
    2. llamar a db_get_productos_by_condicion(condicion) que retorna una lista_productos
    """
    minimo_stock = int(input(Fore.MAGENTA + "\nIngrese el unmbral de mínimo stock: "))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print(Fore.RED + "No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(Fore.YELLOW + str(producto))