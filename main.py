from scrapper_functions import provincias
import time

# Obtenemos listado de provincias
provincias_arg = provincias.get_lista_provincias()

if not provincias_arg.empty:  # Se ha logrado obtener detalle de provincias
    # Atributos a añadir del detalle provincia
    provincias_arg["IDH"] = None
    provincias_arg["analfabetismo"] = None

    # Obtener info detallada de cada provincia
    for index, provincia in provincias_arg.iterrows():

        print(provincia["provincia"], index)
        data_provincia = provincias.get_detalle_provincia(provincia['url'], verbose=False)

        # Enriquecer con información de tabla detalle cada provincia
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "IDH", "IDH (2018)")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "analfabetismo", "Analfabetismo")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "porc_pobacion_argentina", "% de la población argentina")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "autonomía", "Declaración de autonomía")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "altitud media", "• Media")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "altitud maxima", "• Máxima")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "altitud minima", "• Mínima")
        provincias_arg = provincias.add_info_provincia(index, provincias_arg, data_provincia, "coordenadas", "Coordenadas")

        # Esperar 5 segundo entre peticiones
        time.sleep(5)

    print(provincias_arg.head())
    provincias_arg.to_csv("./datasets/provincias_argentina.csv", index=False)