#pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import json

import os
import fiona
from descartes import PolygonPatch
import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt


def get_lista_especies():
    '''
    Devuelve una lista de los href de las especies nativas.
    '''
    
    #URL donde se encuentra la lista de especies
    url = "https://cma.sarem.org.ar/es/listado-de-especies-tratadas?type_1=ficha_de_especie"
    
    #VER ESTA PARTE CON ANTONIO
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
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

    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    #obtengo los elementos usando xpath
    especie = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/h1').text
    categoria=driver.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[3]/a[2]').text
    mapa=driver.find_element_by_xpath('/html/body/script[1]').get_attribute('innerHTML')

    #devuelvo un distionario.
    d={'species': especie,'categoria': categoria,'datos': mapa}
    
    #cierro
    driver.close()
    
    return d 

def get_datos(lista):
    """
    Toma la lista de especies y aplica la función get_datos_especie a cada una de ellas
    """
    #l=get_lista_especies()
    
    final=[]
    
    for i in lista:
        a=get_datos_especie(i)
        
        #si la cat es "no aplicable" o "no"
        if a['categoria'] not in ['EX (Extinta)', 'NA (No Aplicable)','NE (No Evaluada)']:
            final.append(a)
        
        #agregar un time lapse
        
    
    with open('especies.json', 'w') as outfile:
        json.dump(final, outfile)


def get_lista_poligonos(lista):
    '''Prepara una lista de poligonos para ser descargados/ploteados.
    
    Argumentos:
    --lista: '''
    
    if a["leaflet"]["leaflet-map-view-cabecera-de-ficha-mapa-block-1"]['features'][0]['type']=='polygon':
        #para poligonos
        pols=a["leaflet"]["leaflet-map-view-cabecera-de-ficha-mapa-block-1"]['features']
        latlon=[[[i["lon"],i["lat"]] for i in pols[x]['points']] for x in range(0,len(pols))]
        return latlon
    elif a["leaflet"]["leaflet-map-view-cabecera-de-ficha-mapa-block-1"]['features'][0]['type']=='multipolygon':
        #para multipoligonos
        pols=a["leaflet"]["leaflet-map-view-cabecera-de-ficha-mapa-block-1"]['features'][0]['component']
        latlon=[[[i["lon"],i["lat"]] for i in pols[x]['points']] for x in range(0,len(pols))]
        return latlon


def plot_mapa (latlon, nombre):
    '''Plotea el o los poligonos que contiene "latlon" que es una lista de poligonos
    
    Argumentos:
    -- latlon: lista de poligonos.
    -- nombre: nombre de la especie a plotear
    '''
    
    r = [sg.Polygon(latlon[i]) for i in range(0, len(latlon))]

    new_shape= so.unary_union(r)

    BLUE = '#6699cc'
    GRAY = '#999999'
    fig = plt.figure(figsize=(5, 5)) 

    #para verlo mas grande
    #fig, ax=plt.subplots(dpi=150)

    ax = fig.gca() 
    ax.add_patch(PolygonPatch(new_shape, fc=BLUE, alpha=0.5, linewidth=0.3))
    ax.axis('scaled')
    ax.set_title(nombre)

    return plt.show()


def guardar_shp (latlon, nombre):
    '''Guarda en .shp el o los poligonos que contiene "latlon" que es una lista de poligonos
    
    Argumentos:
    -- latlon: lista de poligonos.
    -- nombre: nombre de la especie 
    '''

    r = [sg.Polygon(latlon[i]) for i in range(0, len(latlon))]
    new_shape= so.unary_union(r)
    
    # Write a new Shapefile
    new_folder = 'MAPAS_ESPECIES'
    os.makedirs(new_folder,exist_ok=True)
    
    name='MAPAS_ESPECIES/{}.shp'.format(nombre)
    
    schema = {
        'geometry': 'Polygon',
        'properties': {'id': 'int'},
    }
    
    with fiona.open(str(name), 'w', 'ESRI Shapefile', schema) as c:
        ## If there are multiple geometries, put the "for" loop here
        c.write({
            'geometry': sg.mapping(new_shape),
            'properties': {'id': 123},
        })

