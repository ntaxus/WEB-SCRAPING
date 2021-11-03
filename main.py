from scrapper_functions import especies, provincias, areas_protegidas, setup_driver
import sys
import os


# creamos un directorio donde se guardarán los datasets
dirName = 'datasets'

if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("El fichero" , dirName ,  "ha sido creado.")
else:    
    print("El fichero" , dirName ,  "ya existe")



# Inicializamos el webdriver teniendo en cuenta si se pasa IP para proxy
direcciones_ip = sys.argv

if len(direcciones_ip) >= 2:  # Con PROXY si se IP pasa al ejecutar programa
    driver = setup_driver(PROXY=direcciones_ip[1])
else:  # Sin proxy
    driver = setup_driver()

#########################################################
# PROVINCIAS ARGENTINA
#########################################################

# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias(driver)

# Obtener detalle de cada provincia
provincias.get_detalle_provincias(driver, provincias_arg)

# Inicializamos otro driver con nueva IP si se pasa más de una IP al programa
if len(direcciones_ip) >= 3:
    driver = setup_driver(PROXY=direcciones_ip[2])

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

areas_protegidas.get_areas_protegidas()
