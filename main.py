from scrapper_functions import especies, provincias
import requests


#########################################################
# PROVINCIAS ARGENTINA
#########################################################

# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias()

# Obtener detalle de cada provincia
provincias.get_detalle_provincias(provincias_arg)


#########################################################
# DISTRIBUCIÓN ESPECIES
#########################################################

# Obtenemos listado de las especies de mamíferos
especies_arg = especies.get_lista_especies()

# Scraper información detallada de cada especie
especies.get_datos(especies_arg)


#########################################################
# AREAS PROTEGIDAS ARGENTINA
#########################################################

url = "https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_WDOECM_Oct2021_Public_ARG_shp.zip"
zip_file = requests.get(url)

with open("datasets/areas_protegidas.zip", "wb") as file:
    file.write(zip_file.content)