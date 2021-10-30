import json
import scrapper_functions
import time


def get_lista_especies():
    '''
    Devuelve una lista de los href de las especies nativas.
    '''
    
    #URL donde se encuentra la lista de especies
    url = "https://cma.sarem.org.ar/es/listado-de-especies-tratadas?type_1=ficha_de_especie"
    
    #Inicializamos driver
    driver = scrapper_functions.setup_driver()
    driver.get(url)
    
    #obtengo los elementos usando xpath
    elems = driver.find_elements_by_xpath("//span[@class='nombrecientifico-listado']/a[@href]")
    
    #guardo en una lista
    a=[i.get_attribute("href") for i in elems]
    
    #cierro la ventana
    driver.close()
    
    #devuelvo una lista de href
    return a

def get_datos_especie(url):
    '''Devuelve un dictionario con en nombre de la especie, la categoría de conservación 
    y los datos georeferenciados   
    '''
    
    #URL donde se encuentra la lista de especies
    #url = 'https://cma.sarem.org.ar/es/especie-nativa/abrawayaomys-ruschii'

    # Inicializamos driver
    driver = scrapper_functions.setup_driver()
    driver.get(url)

    #obtengo los elementos usando xpath
    especie = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/h1').text
    categoria = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[3]/a[2]').text
    mapa = driver.find_element_by_xpath('/html/body/script[1]').get_attribute('innerHTML')

    #devuelvo un distionario.
    d = {'species': especie,'categoria': categoria,'datos': mapa}
    
    #cierro
    driver.close()
    
    return d 

def get_datos(lista):
    """
    Toma la lista de especies y aplica la función get_datos_especie a cada una de ellas. Excluye aquellas en cat. "EX", "NA" y "NE".
    """
    
    #creo una lista vacía 
    final=[]
    
    #itero para cada una de las especies en la lista
    for i in lista:
        a=get_datos_especie(i)
        
        #guardo en la lista solo si la categoría de la especie no es NA, NE o EX.
        if a['categoria'] not in ['EX (Extinta)', 'NA (No Aplicable)','NE (No Evaluada)']:
            final.append(a)
        
        #agrego un time lapse
        time.sleep(2)

    #guardo en un archivo json
    with open('datasets/especies.json', 'w') as outfile:
        json.dump(final, outfile)
