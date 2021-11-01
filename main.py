import scrapper_functions
from scrapper_functions import especies, provincias
import requests


# Inicializamos el webdriver
driver = scrapper_functions.setup_driver()

#########################################################
# PROVINCIAS ARGENTINA
#########################################################

# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias(driver)

# Obtener detalle de cada provincia
provincias.get_detalle_provincias(driver, provincias_arg)


#########################################################
# DISTRIBUCIÓN ESPECIES
#########################################################

# Obtenemos listado de las especies de mamíferos
especies_arg = especies.get_lista_especies(driver)

# Scraper información detallada de cada especie
especies.get_datos(driver, especies_arg)


#########################################################
# AREAS PROTEGIDAS ARGENTINA
#########################################################

# Descargamos directamente zip de la web
url = "https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_WDOECM_Oct2021_Public_ARG_shp.zip"
zip_file = requests.get(url)

# Lo guardamos en carpeta datasets
with open("datasets/areas_protegidas.zip", "wb") as file:
    file.write(zip_file.content)