from scrapper_functions import provincias

# Obtenemos listado de provincias
for provincia, info in provincias.get_lista_provincias().items():
    print(provincia, info)
