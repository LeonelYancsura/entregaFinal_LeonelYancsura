"""
Módulo: main.py
Descripción: Este es el módulo principal que coordina la ejecución del sistema de gestión de inventarios.
Inicia el menú principal y permite al usuario interactuar con diversas funciones, como agregar, eliminar, actualizar y buscar productos.
Las opciones del menú son manejadas a través de un bucle interactivo que se repite hasta que el usuario decide salir.
"""

# Importamos las funciones necesarias del módulo `funcionesMenu`.
from funcionesMenu import*
from funcionesDataBase import db_crear_tabla_productos


#---------------------------------------------------------------------------------------------------------------------
#Declaramos la funcion principal
def main():
    """
        Función principal que inicia el programa de gestión de inventario.

        1. Inicializa la base de datos creando la tabla 'productos' si no existe.
        2. Muestra un menú interactivo al usuario con diferentes opciones.
        3. Ejecuta la opción seleccionada por el usuario.
        4. Permite salir del programa de forma segura.

        Maneja errores y asegura una experiencia de usuario fluida.
        """
    try:
        # Inicializamos la base de datos y creamos la tabla si no existe.
        db_crear_tabla_productos()
        print("Base de datos inicializada correctamente.")

        # Bucle principal del programa.
        while True:
            try:
                # Mostramos el menú de opciones y obtenemos la selección del usuario.
                opcion = menu_mostrar_opciones()
                print(f"\nUsted seleccionó: {opcion}")

                # Procesamos la opción seleccionada.
                if opcion == "1":
                    menu_registrar_producto()
                elif opcion == "2":
                    menu_mostrar_productos()
                elif opcion == "3":
                    menu_actualizar_producto()
                elif opcion == "4":
                    menu_eliminar_producto()
                elif opcion == "5":
                    menu_buscar_producto()
                elif opcion == "6":
                    menu_reporte_bajo_stock()
                elif opcion == "7":
                    print("Gracias por usar el sistema. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, elija una opción válida.")

            except Exception as e:
                print(f"Error inesperado al procesar la opción: {e}")

            # Preguntamos al usuario si desea continuar o salir.
            continuar = input("\nIngrese 's' para salir o cualquier otra tecla para continuar: ").lower()
            if continuar == "s":
                print("\nGracias por usar el sistema. ¡Hasta luego!")
                break

    except Exception as e:
        #Manejamos errores globales al iniciar el programa.
        print(f"Error crítico al iniciar el programa: {e}")

# =============================================================================
# INVOCAMOS LA FUNCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    main()  # Llamado de la función principal.