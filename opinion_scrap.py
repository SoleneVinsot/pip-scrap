
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests
import html
import csv
import numpy as np 

#utiliser le chrome driver qui est dans mon document à l'endroit : /Users/solenevinsot/Desktop/Python/CNIL_Essaie/chromedriver
#'driver.implicitly_wait(3)' pour mettre un temps d'attente dans ma demande 
#driver.get pour aller sur l'url
driver = webdriver.Chrome(executable_path=r"/Users/solenevinsot/Desktop/Python/CNIL_Essaie/chromedriver")
driver.implicitly_wait(3)
driver.get('https://www.opinionsystem.fr/fr-fr/search')

#trouver les éléments par id "find_element_by_id"
#'send keys' pour dire de mettre immobilier dans la barre de recherche
entreprise = driver.find_element_by_id("query")
entreprise.send_keys("immobilier")

"""ville=driver.find_element_by_id('location')
ville.send_keys('Paris, France')""" 

#by xpath car il n'y a pas d'id dans le code du site
driver.find_element_by_xpath("/html/body/div[1]/section[2]/div/div/div/div/div/div/div[1]/div[3]/form/div[3]/button").click()


n=0
while n<120 :
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/div/div/div/button").click()
    n=n+1


#"get_attribut" pour prendre tous les href
liste_liens=[]
j=3
while j<1070 : 
    id=driver.find_element_by_xpath('/html/body/div[1]/section[3]/div[1]/div/div['+str(j)+']/a')
    lien = id.get_attribute('href')
    j=j+1
    liste_liens.append(lien)
#https://www.opinionsystem.fr/certificate.php?collaborator_id=11146
time.sleep(8)
#print(liste_liens)
print(len(liste_liens))

driver.quit()

np.save("liens_france",liste_liens)