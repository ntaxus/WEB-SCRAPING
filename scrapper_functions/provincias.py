from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


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

    return float(str.replace(",", "."))


def get_lista_provincias():
    '''
    Obtiene información básica de las provincias de Argentina.
    :return: diccionario con clave por provincia y valor diccionario datos básicos.
    '''

    provincias = dict()

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
            provincias[provincia] = {"url": enlace,
                                     "poblacion": poblacion,
                                     "superficie": superficie,
                                     "densidad": densidad,
                                     "capital": capital}

    except NoSuchElementException:
        print("Error no se encuentra elemento")

    return provincias
