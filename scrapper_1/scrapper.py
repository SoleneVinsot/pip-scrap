import time
import re
import requests
import html
import csv
import numpy as np
import os
import pandas as pd

# Nom du fichier de sauvegarde
saveAs = 'contacts_immobilier_France.xlsx'

# Récupération du path du fichier
script_dir = os.path.dirname(__file__)

# Nom du fichier contenant les liens
filenameLinks = 'liens_france.npy'

# Création du path pour récupérer le fichier des liens
file_path = os.path.join(script_dir, filenameLinks)

# Récupération des liens sous forme d'objet
linksObject = np.load(file_path)

# Transforme notre object en liste
links = list(linksObject)

requests_headers = {'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

address = []
city = []
country = []
number = []
company = []
email = []


for i in links :
    try :
        request = requests.get(i, headers = requests_headers, timeout = 10)
        bodyString = request.text
        bodyString = html.unescape(bodyString)
        bodyString = bodyString.replace('\n', '')
        bodyString = bodyString.replace('\t', '')
        bodyString = bodyString.replace('\r', '')

        companyResult = re.findall('<span itemprop="itemreviewed" ><em>(.+?(?=</em></span>))', bodyString)
        company.extend(companyResult)

        addressResult = re.findall('</div><div class="Information"><span>(.+?(?=</span></div>))', bodyString)
        address.append(addressResult[0])
        city.append(addressResult[1])
        country.append(addressResult[2])
        number.append(addressResult[3])

        emailResult = re.findall('E-mail</span></div><div class="Colon"><span>:</span></div><div class="Information"><a href="mailto:(.+?(?=">))', bodyString)
        email.extend(emailResult)
    except :
        pass

df = pd.DataFrame.from_dict({
  'Nom': company,
  'Email': email,
  'Adresse': address,
  'Numéro': number,
  'Ville': city,
  'Pays': country
})

file_path_save = os.path.join(script_dir, saveAs)
df.to_excel(file_path_save)

