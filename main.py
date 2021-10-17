from scrapper_functions import provincias
import time

# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias()

# Atributos a añadir del detalle provincia
provincias_arg["IDH"] = None
provincias_arg["analfabetismo"] = None

# Obtener info detallada de cada provincia
for index, provincia in provincias_arg.iterrows():

    print(provincia["provincia"], index)
    data_provincia = provincias.get_detalle_provincia(provincia['url'], verbose=False)

    # TODO: pasar a función de la librería
    try:
        provincias_arg.loc[index, "IDH"] = data_provincia["IDH (2018)"]
    except KeyError:
        print("IDH no disponible") # El dato no está disponible en la web

    try:
        provincias_arg.loc[index, "analfabetismo"] = data_provincia["Analfabetismo"]
    except KeyError:
        print("Analfabetismo no disponible") # El dato no está disponible en la web

    # Esperar 5 segundo entre peticiones
    time.sleep(5)

print(provincias_arg.head())