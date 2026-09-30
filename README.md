# 📦 Gestión de Inventario en Sucursales

## Programa desarrollado en Python que permite administrar sucursales y llevar un inventario de productos organizados por categorías.  El proyecto utiliza una interfaz gráfica y archivos XML validados mediante un DTD para estructurar y cargar la información del inventario.
<img src="src/imagen/oxxo.png" width="450">

### 👾 Tecnologías usadas

- *Lenguaje: **Python***
- *Librerías: **Tkinter, Pillow, xml.etree.ElementTree, lxml, os y time.***
- *Archivos utilizados: **XML y DTD.***

### Características principales
- Interfaz gráfica: Utiliza la librería tkinter para crear ventanas, botones, formularios y menús para interactuar con el sistema.
- Programación orientada a objetos: El proyecto está organizado mediante diferentes clases para representar las sucursales, categorías, productos, el administrador de sucursales y el menú de la aplicación.
- Administración de sucursales: Permite agregar nuevas sucursales y verificar que no existan sucursales con el mismo nombre.
- Gestión de productos: Permite agregar productos al inventario seleccionando una sucursal y una categoría, además de registrar su precio y cantidad disponible.
- Organización por categorías: Los productos se encuentran agrupados dentro de categorías pertenecientes a cada sucursal.
- Validación de datos: Verifica que los campos estén completos y que el precio y el stock tengan valores válidos y no negativos.
- Validación de nombres: Comprueba que el nombre de una sucursal contenga únicamente letras y espacios.
- XML: La información del inventario se encuentra estructurada mediante un archivo XML con sucursales, categorías y productos.
- DTD: Utiliza un archivo DTD para comprobar que la estructura del XML sea válida antes de cargar la información al programa.
- Pantalla de carga: Al iniciar el programa se muestra una pantalla de carga con una imagen y una barra de progreso.
<img width="400" height="253" alt="Screenshot 2026-09-29 at 7 52 10 p m" src="https://github.com/user-attachments/assets/db8bec97-a121-4d1e-aabf-f7af1a0d1512" />

### Instalación

**Para ejecutar el proyecto:✅**

1. Descarga o clona este repositorio.<br>
***git clone https://github.com/Halinxx14/Gestion-de-Inventario-en-Sucursales.git***
2. Ingresa a la carpeta del proyecto:<br>
***cd Gestion-de-Inventario-en-Sucursales***
3. Asegúrate de tener instalado Python.<br>
4. Instala las librerías necesarias:<br>
***pip install pillow lxml***
5. Ejecuta el archivo principal:<br>
***python main.py***

### Uso

**Al iniciar el programa se muestra una pantalla de carga y posteriormente el menú principal.**

El menú cuenta con las siguientes opciones:
<img width="400" height="420" alt="Screenshot 2026-09-29 at 7 52 18 p m" src="https://github.com/user-attachments/assets/d6952566-79ac-4d41-82e7-e9ecb0c15ee2" />

***Agregar sucursal***

Permite ingresar el nombre de una nueva sucursal. El programa verifica que el nombre sea válido y que no exista otra sucursal con el mismo nombre.

***Agregar producto***

Permite seleccionar una sucursal e ingresar:

<img width="419" height="515" alt="Screenshot 2026-09-29 at 7 52 43 p m" src="https://github.com/user-attachments/assets/e10b8db5-569d-4fc1-8f76-7c10479b086f" />

*El programa valida los datos antes de agregar el producto al inventario.*

***Mostrar inventario***

Permite visualizar la información organizada de las sucursales, categorías y productos registrados.

***Validación XML y DTD***

Antes de cargar la información del inventario, el programa valida el archivo inventario.xml utilizando inventario.dtd.

Si el XML cumple con la estructura definida por el DTD, el programa continúa con la carga del inventario. Si existe algún error de estructura o sintaxis, se muestra un mensaje de error y el programa no continúa con la carga.
<img width="760" height="319" alt="Screenshot 2026-09-29 at 8 03 47 p m" src="https://github.com/user-attachments/assets/d4ed3b63-fae5-4ae7-9ec4-9a1a380daaa8" />

### Contribuciones

¡Las contribuciones son bienvenidas! Si deseas ayudar a mejorar este proyecto, puedes seguir los siguientes pasos:

1. Haz un fork del repositorio: Crea una copia del repositorio en tu cuenta de GitHub.<br>
2. Clona tu fork:<br>
***git clone https://github.com/Halinxx14/Gestion-de-Inventario-en-Sucursales.git***
3. Crea una nueva rama:<br>
***git checkout -b nombre-de-tu-rama***
4. Realiza tus cambios y crea un commit:<br>
***git add .***
***git commit -m "Descripción de tus cambios"***
5. Envía los cambios a tu repositorio:<br>
***git push origin nombre-de-tu-rama***
6. Abre un Pull Request desde GitHub para proponer tus cambios.

### 📋 Licencia

Este proyecto utiliza la Licencia MIT.

