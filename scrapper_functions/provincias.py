from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


def str_to_int(str):
    '''
    Elimina espacios en blanco y convierte a entero
    :param str:
    :return: int
    '''

    return int(str.replace(" ", ""))


def str_to_float(str):
    '''
    Reemplaza separador decimal a punto y convierte a float

    :param str:
    :return: float
    '''

    return round(float(str.replace(",", ".")), 2)


def get_detalle_provincia(url = "https://es.wikipedia.org/wiki/Provincia_de_Buenos_Aires", verbose=False):
    '''
    Scrapper información detallada de la provincia

    :type verbose: Bool, si True imprime mensajes por pantalla
    :param url: enlace wikipedia página de la provincia
    :return: dict con información de detalle de la provincia
    '''

    # DataFrame datos provincias
    data_provincia = dict()

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)

    tabla_detalle = driver.find_element_by_class_name("infobox.geography.vcard")
    cuerpo_tabla_detalle = tabla_detalle.find_element_by_tag_name("tbody")
    rows = cuerpo_tabla_detalle.find_elements_by_tag_name('tr')

    for row in rows:
        try:
            clave = str.strip(row.find_elements_by_tag_name("th")[0].text)
            valor = str.strip(row.find_elements_by_tag_name("td")[0].text)
            data_provincia[clave] = valor
            print(clave, "--->", valor) if verbose else None
        except:
            print("nothing to show here") if verbose else None

    return data_provincia


def get_lista_provincias():
    '''
    Obtiene información básica de las provincias de Argentina.

    :return: dataframe con la información de cada provincia.
    '''

    provincias = pd.DataFrame(columns=["provincia", "url", "poblacion",
                                       "superficie", "densidad", "capital"])

    try:
        # Ruta del driver
        driver = webdriver.Chrome('chromedriver.exe')
        # Cargar web
        driver.get('https://es.wikipedia.org/wiki/Provincias_de_Argentina')

        # Iterar tabla de provincias
        tabla_provincias = driver.find_element_by_class_name("wikitable.sortable.jquery-tablesorter")
        cuerpo_tabla_provincias = tabla_provincias.find_element_by_tag_name("tbody")
        rows = cuerpo_tabla_provincias.find_elements_by_tag_name('tr')  # filas de la tabla

        for row in rows:
            # Columnas por fila
            cols = row.find_elements_by_tag_name("td")

            provincia = cols[0].text
            poblacion = str_to_int(cols[3].text)
            superficie = str_to_int(cols[5].text)
            densidad = str_to_float(cols[7].text)
            capital = cols[8].text
            enlace = row.find_element_by_tag_name("a").get_attribute("href")

            provincias = provincias.append({"provincia": provincia,
                                            "url": enlace,
                                            "superficie": superficie,
                                            "poblacion": poblacion,
                                            "densidad": densidad,
                                            "capital": capital}, ignore_index=True)

        return provincias

    except NoSuchElementException:
        print("Error no se encuentra tabla provincias. Reintentando...")
        time.sleep(3)
        return get_lista_provincias()


def add_info_provincia(index, provincias_arg, data_provincia, columna_df, columna_provincia, verbose=False):
    '''
    Añade información de provincia si está disponible del scrapping

    :param index:
    :param provincias_arg:
    :param data_provincia:
    :param columna_df:
    :param columna_provincia:
    :return: dataframe información provincias Argentina
    '''
    try:
        provincias_arg.loc[index, columna_df] = data_provincia[columna_provincia]
    except KeyError:
        # El dato no está disponible en la web
        print("{} no disponible".format(columna_provincia)) if verbose else None

    return provincias_arg