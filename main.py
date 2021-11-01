from scrapper_functions import especies, provincias, areas_protegidas, setup_driver

# Inicializamos el webdriver
driver = setup_driver()

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

areas_protegidas.get_areas_protegidas()