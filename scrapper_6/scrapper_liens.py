import requests
import html
import pdb
import re
import numpy as np

import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from random import randint
from selenium.webdriver.chrome.options import Options





#Utilisation de selenium pour scrowller toute la page

chrome_options = Options()

#chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920x1080")

urlToScrap='https://www.alltricks.com/C-40958-road'

driver = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'), chrome_options = chrome_options)
driver.implicitly_wait(randint(2,9))
driver.get(urlToScrap)

#Clique sur le bouton pour scrowller
driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[3]/div[6]/a').click()


#Enregistrement des liens
liens=[]
i=1
while i<60 :
  try :
    user=driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/div[2]/div[3]/div[1]/div['+str(i)+']/div/a')
    link = user.get_attribute('href')
    i=i+1
    liens.append(link)
  except :
    i=i+1
    continue

#Sauvegarde des liens avec Numpy
np.save("liens.npy", liens)



