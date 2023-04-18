==============================
API para consultar la Unidad de Fomento en Python (Fapro Test)
==============================

Este proyecto es una API desarrollada en Python utilizando Flask para consultar el valor de la Unidad de Fomento (UF) en Chile para una fecha específica. Fue creado como parte de una prueba para la empresa Fapro.

Requisitos
----------
* Python 3.6+
* Flask
* requests
* BeautifulSoup4

Instalación
-----------
1. Clona este repositorio.

2. Crea un entorno virtual y actívalo:

   .. code-block:: shell

      python -m venv venv
      source venv/bin/activate  # en Windows: venv\Scripts\activate

3. Instala las dependencias:

   .. code-block:: shell

      pip install -r requirements.txt

Uso
---
1. Ejecuta la aplicación:

   .. code-block:: shell

      python app.py

2. La API estará disponible en http://127.0.0.1:5000/. Puedes enviar solicitudes GET a /uf con un parámetro de fecha en formato 'YYYY-MM-DD'. Por ejemplo:

   .. code-block:: shell

      curl "http://127.0.0.1:5000/uf?date=2023-04-01"

Estructura del proyecto
-----------------------
- app.py: Archivo principal que contiene la aplicación Flask y la ruta de la API.
- services/uf_service.py: Contiene la clase UFService que se encarga de obtener el contenido HTML de la página con los valores de UF.
- parsers/uf_parser.py: Contiene la clase UFParser que se encarga de analizar el contenido HTML y extraer el valor de la UF para una fecha específica.
- tests/: Carpeta que contiene las pruebas unitarias del proyecto.

Pruebas
-------
Para ejecutar las pruebas unitarias, corre el siguiente comando en la carpeta principal del proyecto:

   .. code-block:: shell

      python -m unittest discover