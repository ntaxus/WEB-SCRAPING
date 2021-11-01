# PRA1 - Tipología y ciclo de vida de los datos
Factores socioeconómicos que influyen en el nivel de protección a nivel provincia de los mamíferos de Argentina.

## Instalación

Ver detalle de las librerías requeridas para el funcionamiento del programa en el fichero *requirements.txt*

## Introducción

Este trabajo consistió en la recopilación de datos georeferenciados acerca de la distribución de las especies de mamíferos presentes en Argentina, combinando esta información a nivel provincial con una serie de indicadores socio-económicos y de protección ambiental. Como resultado del proyecto, se han generado tres conjuntos de datos diferenciados. Con esta información, se pretende dr respuestas a preguntas tales como:

- ¿Existe alguna relación entre las especies en peligro de extinción y la tasa de analfabetimo de las provincias donde habitan?
- ¿Están las especies mejor protegidas en aquellas provincias con un IDH más alto?
- ¿Existe correlación entre las especies con menor extensión de hábitat (km2) y las provincias más pobladas?
- Otras cuestiones que relacionan la distribución de las especies con las provincias donde habitan.


## Descripción de los datasets

El programa genera los siguientes conjuntos de datos:

1. ***provincias_argentina.csv***: Información demográfica y socioeconómica básica de las diferentes provincias de Argentina.
2. ***especies.json***: Información georeferenciada de la distribución de los mamíferos de Argentina, junto con el nombre científico y su categoría de conservación.
3. ***areas_protegidas.zip***: Información georeferenciada de la extensión de las áreas protegidas de Argentina. Debido al tamaño de los archivos GIS, se han troceado en tres partes, de forma que tras su carga se pueda hacer un merge de las diferentes áreas.

## Explicación main.py

En primer lugar se importa la librería ``scrapper_functions`` que permite capturar la información y generar los diferentes conjuntos de datos:

````python
from scrapper_functions import especies, provincias, areas_protegidas, setup_driver
````

A continuación, inicializamos el web driver de Selenium mediante `setup_driver()`. Una vez incializado, podemos ir llamando a las diferentes arañas:

- **Información provincias**: extrae y genera el .csv con la información de las provincias.

````python
# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias(driver)

# Obtener detalle de cada provincia
provincias.get_detalle_provincias(driver, provincias_arg)
````

- **Distribución especies**: genera .json con la distribución de cada especie en Argentina.

````python
# Obtenemos listado de las especies de mamíferos
especies_arg = especies.get_lista_especies(driver)

# Scraper información detallada de cada especie
especies.get_datos(driver, especies_arg)
````

- **Áreas protegidas**: descarga y genera un archivo comprimido .zip con la información georeferenciada de las áreas naturales de Argentina.

````python
areas_protegidas.get_areas_protegidas()
````

## Licencia

Los conjuntos de datos generados se encuentran bajo licencia [CC0: Public Domain License](https://creativecommons.org/share-your-work/public-domain/cc0/).
