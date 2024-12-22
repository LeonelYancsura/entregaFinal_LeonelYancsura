![Logo](https://github.com/talentotech-ba/recursos/blob/0dea22ffba99ff1e32e0c6e4d51f738816e7afa5/tt-banner.jpg?raw=true)
# Proyecto Final Integrador (PFI)

### Objetivos:
- Deberán desarrollar una aplicación en Python que permita gestionar el inventario de una pequeña tienda. 
- La aplicación debe ser capaz de registrar, actualizar, eliminar y mostrar productos en el inventario. 
- Además, debe incluir funcionalidades para realizar búsquedas y generar reportes de stock.

### Requerimientos:
- Crear una base de datos SQLite para almacenar los datos de los productos (nombre, descripción, cantidad, precio, categoría).
- Implementar una interfaz de usuario básica para interactuar con la base de datos desde la terminal (línea de comandos).
- Incluir funcionalidades de registro, actualización, eliminación y visualización de productos.
- Generar reportes de productos con bajo stock.

### Objetivos de aprendizaje:
- Implementar estructuras de control y funciones en Python.
- Desarrollar habilidades de manipulación de archivos y manejo de datos.
- Aplicar conocimientos de bases de datos SQLite.

### Base de datos:
- Crear una base de datos SQLite llamada 'inventario.db' para almacenar los datos de los productos.
- La tabla 'productos' debe contener las siguientes columnas:
  - 'id': Identificador único del producto (clave primaria, autoincremental).
  - 'nombre': Nombre del producto (texto, no nulo).
  - 'descripcion': Breve descripción del producto (texto).
  - 'cantidad': Cantidad disponible del producto (entero, no nulo).
  - 'precio': Precio del producto (real, no nulo).
  - 'categoria': Categoría a la que pertenece el producto (texto).

### Funcionalidades de la aplicación
- **Registro de productos:** La aplicación debe permitir al usuario agregar nuevos productos al inventario, solicitando los siguientes datos: nombre, descripción, cantidad, precio y categoría.
- **Visualización de productos:** La aplicación debe mostrar todos los productos registrados en el inventario, incluyendo su ID, nombre, descripción, cantidad, precio y categoría.
- **Actualización de productos:** La aplicación debe permitir al usuario actualizar la cantidad disponible de un producto específico utilizando su ID.
- **Eliminación de productos:** La aplicación debe permitir al usuario eliminar un producto del inventario utilizando su ID.
- **Búsqueda de productos:** La aplicación debe ofrecer una funcionalidad para buscar productos por su ID, mostrando los resultados que coincidan con los criterios de búsqueda. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
- **Reporte de Bajo Stock:** La aplicación debe generar un reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario.

## Interfaz de usuario:
- Implementar una interfaz de usuario básica para interactuar con la base de datos a través de la línea de comandos(terminal). La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.
  - Opcional: Utilizar la librería 'colorama' para mejorar la legibilidad y experiencia de usuario en la terminal, añadiendo colores a los mensajes y opciones.

  ```
  -------------------------------------
  Menú principal
  -------------------------------------
  1.Agregar producto.
  2.Mostrar productos.
  3.Actualizar cantidad de producto.
  4.Eliminar producto.
  5.Buscar producto.
  6.Reporte de bajo stock.
  7.Salir.
  ```
  

## Entrega:

- El proyecto final debe ser entregado en el campus virtual mediante un LINK. Los archivos que conforman el proyecto deberán estar alojados en una carpeta de Google Drive (público) y debe incluir:
  - El script en Python ('.py') con el código fuente de la aplicación.
  - La base de datos SQLite ('inventario.db'), si es que se ha generado con datos de prueba.
  - Un archivo 'README.txt' explicando cómo ejecutar la aplicación y las funcionalidades implementadas.
