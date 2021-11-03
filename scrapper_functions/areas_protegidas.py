import requests
import zipfile
import os
import shutil


def crear_zip(path, ziph):
    '''
    Comprime directorio en fichero zip

    :param path: directorio que se quiere comprimir
    :param ziph: objeto zipfile que se generará

    :return: None
    '''
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


def get_areas_protegidas():
    '''
    Descarga fichero con áreas protegidas de Argentina en la carpeta datasets/areas_protegidas.
    Posteriormente, vuelve a generar un archivo .zip únicamente con la información necesaria.

    :return: None. El fichero .zip se crea y deja en el directorio datasets/
    '''

    # Descargamos directamente zip de la web
    url = "https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_WDOECM_Oct2021_Public_ARG_shp.zip"

    # Establecemos User-Agent antes de hacer petición
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             "Chrome/95.0.4638.54 Safari/537.36"}

    # Obtenemos fichero y lo guardamos en carpeta datasets
    zip_file = requests.get(url, headers=headers)

    # Extraemos ficheros que nos interesan
    with open("datasets/areas_protegidas.zip", "wb") as file:
        file.write(zip_file.content)

    # Leer zipfile descargado
    with zipfile.ZipFile("datasets/areas_protegidas.zip", "r") as zipObj:

        # Extraer solo los .zip
        i = 0
        for item in zipObj.namelist():

            if item.endswith('.zip'):

                # Extraemos fichero zip
                ruta_dest = 'datasets/areas_protegidas/parte_{}'.format(i)
                file_name = zipObj.extract(item, ruta_dest)

                # Leer zipfile descargado
                with zipfile.ZipFile(file_name, "r") as nested_zipObj:
                    nested_zipObj.extractall(ruta_dest)
                
                # cerramos el archivo
                nested_zipObj.close()
                
                # eliminamos el .zip
                os.remove(file_name)	

                i += 1

        # Comprimir nuevamente archivos
        zipf = zipfile.ZipFile('datasets/areas_protegidas.zip', 'w', zipfile.ZIP_DEFLATED)
        crear_zip('datasets/areas_protegidas/', zipf)
        zipf.close()
        
        #elimino el directorio
        shutil.rmtree('datasets/areas_protegidas/')
