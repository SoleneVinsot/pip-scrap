import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests
import html
import csv
import os
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Options du chromedriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# Nom du fichier de sauvegarde
saveAs = 'Avocats-paris.xlsx'

# Récupération du path du fichier
script_dir = os.path.dirname(__file__)

# URL à scrapper
urlToScrap = 'http://www.avocatsparis.org/Eannuaire/CMSRecherche2.aspx?wmode=transparent'

# Liste des liens
links = []

# Chromedriver doit être installé et placé à la racine du projet
driver = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'), options = chrome_options)
driver.implicitly_wait(3)
driver.get(urlToScrap)

activities = [
  "Droit de la circulation et des transports",
  "Dommages corporels et matériels",
  "Droit de la consommation",
  "Contentieux,  médiation,  arbitrage",
  "Droit de la faillite et du surendettement",
  "Droit de la famille",
  "Droit de la sécurité sociale",
  "Droit de l'environnement",
  "Droit de l'immigration et d'asile",
  "Droit de l'UE",
  "Droit des affaires",
  "Droit des biens",
  "Droit des successions",
  "Droit des technologies de l'information",
  "Droit du travail",
  "Droit fiscal",
  "Droit pénal",
  "Droit public",
  "Droits de l'homme et libertés publiques",
  "Propriété intellectuelle"
]

for activity in activities :

    # Choix de l'arrondissement
    webInputElement = driver.find_element_by_id("_ctl0_Corps_txtRSArrondissement")
    webInputElement.send_keys("75008")

    # Choix de l'activity
    webOptionElement = driver.find_element_by_id("_ctl0_Corps_ddlRSActivite")
    webOptionElement.send_keys(activity)
    time.sleep(1)

    # Selectionne parmi les choix proposes
    driver.find_element_by_id("_ctl0_Corps_imgbtnRecherche").click()

    def getLinksFromCards():
      j = 2
      while True :
          try :
            anchor = driver.find_element_by_xpath('//*[@id="_ctl0_Corps_dgListeResultat"]/tbody/tr['+str(j)+']/td/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
            link = anchor.get_attribute('href')
            links.append(link)
            j += 1
          except :
            break

    currentPage = 1
    while True :
        try :
          getLinksFromCards()
          driver.find_element_by_id("_ctl0_Corps_DataGridPager1_Page_" + str(currentPage + 1)).click()
          currentPage += 1
        except :
          break

    driver.find_element_by_id('_ctl0_Corps_ImageButton1').click()


driver.quit()

requests_headers={'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

names = []
addresses = []
numbers = []
faxes = []
emails = []
activities = []
acts = []

for link in links :
    req = requests.get(link, headers = requests_headers, timeout = 10)
    body = req.text
    body = html.unescape(body)

    # Noms
    pattern = '<span id="_ctl0_Corps_lblNom" tabindex="2">(.+?(?=</span>))'
    name = re.findall(pattern, body)
    names.extend(name)

    # Adresse
    pattern = '<span id="_ctl0_Corps_lblAdresse" tabindex="2">(.+?(?=</span>))'
    address = re.findall(pattern, body)
    addresses.extend(address)

    # Numéro de téléphone
    pattern = '<span id="_ctl0_Corps_lblTelephone" tabindex="2">(.+?(?=</span>))'
    number = re.findall(pattern, body)
    numbers.extend(number)

    # Fax
    pattern = '<span id="_ctl0_Corps_lblTelecopie" tabindex="2">(.+?(?=</span>))'
    fax = re.findall(pattern, body)
    faxes.extend(fax)

    # Activités
    pattern = '<span id="_ctl0_Corps_lblActivitesDominantes" tabindex="2">(.+?(?=</span>))'
    act = re.findall(pattern, body)
    acts.extend(act)

    # Email
    pattern = '<a href="mailto:(.+?(?=">))'
    if 'href="mailto:' in body :
        email = re.findall(pattern, body)
        emails.extend(email)
    else :
        emails.append('NA')

for act in acts:
    act = act.replace('<br />', ' ; ')
    activities.append(act)



df = pd.DataFrame.from_dict({
  'Nom': names,
  'Email': emails,
  'Adresse': addresses,
  'Numéro': numbers,
  'Fax': faxes,
  'Activité': activities
})

file_path_save = os.path.join(script_dir, saveAs)
df.to_excel(file_path_save)