import json
import time


def get_lista_especies(driver):
    '''
    Devuelve una lista de los href de las especies nativas.

    :param driver:
    :return:
    '''
    
    # URL donde se encuentra la lista de especies
    url = "https://cma.sarem.org.ar/es/listado-de-especies-tratadas?type_1=ficha_de_especie"
    
    # Inicializamos driver
    driver.get(url)
    
    # obtengo los elementos usando xpath
    elems = driver.find_elements_by_xpath("//span[@class='nombrecientifico-listado']/a[@href]")
    
    # guardo en una lista
    a = [i.get_attribute("href") for i in elems]
    
    # devuelvo una lista de href
    return a


def get_datos_especie(driver, url):
    '''
    Devuelve un dictionario con en nombre de la especie, la categoría de conservación
    y los datos georeferenciados

    :param driver:
    :param url:
    :return: diccionario info especie
    '''

    # Inicializamos driver
    driver.get(url)

    # obtengo los elementos usando xpath
    especie = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/h1').text
    categoria = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[3]/a[2]').text
    mapa = driver.find_element_by_xpath('/html/body/script[1]').get_attribute('innerHTML')

    # Imprimir pantalla especie
    print(especie)

    # devuelvo un diccionario
    return {'species': especie, 'categoria': categoria, 'datos': mapa}


def get_datos(driver, lista):
    '''
    Toma la lista de especies y aplica la función get_datos_especie a cada una de ellas.
    Excluye aquellas en cat. "EX", "NA" y "NE".

    :param driver:
    :param lista:
    :return: None
    '''
    
    # creo una lista vacía
    final = []
    
    # itero para cada una de las especies en la lista
    for i in lista:
        a = get_datos_especie(driver, i)
        
        # guardo en la lista solo si la categoría de la especie no es NA, NE o EX.
        if a['categoria'] not in ['EX (Extinta)', 'NA (No Aplicable)', 'NE (No Evaluada)']:
            final.append(a)
        
        # agrego un time lapse
        time.sleep(2)

    # guardo en un archivo json
    with open('datasets/especies.json', 'w') as outfile:
        json.dump(final, outfile)
