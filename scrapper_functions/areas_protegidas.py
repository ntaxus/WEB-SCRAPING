import scrapper_functions
import time

def get_areas_protegidas():

    #URL
    url='https://www.protectedplanet.net/country/ARG'

    # Inicializamos driver
    driver = scrapper_functions.setup_driver()
    driver.get(url)

    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[2]/button").click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="v-app"]/div[2]/div/div/div/div/div[2]/div[1]/div/ul/li[2]/span').click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="v-app"]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/button').click()

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="v-app"]/div[4]/div[2]/ul/li/a/span').click()

    time.sleep(5)

    # https://d1gam3xoknrgr2.cloudfront.net/current/WDPA_WDOECM_Oct2021_Public_ARG_shp.zip
    driver.close()