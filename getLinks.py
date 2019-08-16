
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests
import html
import csv
import numpy as np

## modif Solenee

# Nom du fichier de sauvegarde
filename = 'liens_france'
# A changer selon votre path
path = '/Users/seald/Desktop/scrap-python/chromedriver'
# URL à scrapper
urlToScrap = 'https://www.opinionsystem.fr/fr-fr/search'

driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(3)
driver.get(urlToScrap)

# On récupère l'element input avec l'id `query`
webElement = driver.find_element_by_id("query")
# On injecte une valeur à l'input
webElement.send_keys("immobilier")

# On récupère le button du formulaire de recherche et on clique dessus
driver.find_element_by_xpath("/html/body/div[1]/section[2]/div/div/div/div/div/div/div[1]/div[3]/form/div[3]/button").click()


# Il y a 1100 résultats au total et 9 fiches par pages, soit 120 pages.
nb_pages = 120
num_page = 0

# Rafrachir toutes les pages
while num_page < nb_pages :
  driver.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/div/div/div/button").click()
  num_page += 1

links = []
# 3 car la première card commence à la div 3 du container
num_card = 3
# 1070 cards au total
total_card = 1070

while num_card < total_card :
    ## On récupère l'element lien de la card
    linkElement = driver.find_element_by_xpath('/html/body/div[1]/section[3]/div[1]/div/div['+str(num_card)+']/a')
    ## On extrait l'url texte de l'element lien
    link = linkElement.get_attribute('href')
    ## On ajoute le lien à la liste
    links.append(link)
    num_card += 1

driver.quit()
## On sauvarde les liens dans un ficher `npy`
np.save(filename, links)