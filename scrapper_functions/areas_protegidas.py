import requests


def get_areas_protegidas():
    # Descargamos directamente zip de la web
    url = "https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_WDOECM_Oct2021_Public_ARG_shp.zip"

    # Establecemos User-Agent antes de hacer petición
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/95.0.4638.54 Safari/537.36"}

    # Obtenemos fichero y lo guardamos en carpeta datasets
    zip_file = requests.get(url, headers=headers)

    with open("datasets/areas_protegidas.zip", "wb") as file:
        file.write(zip_file.content)