import time
import re
import requests
import html
import csv
import numpy as np
import os
import pandas as pd

# Nom du fichier de sauvegarde
saveAs = 'contacts_immobilier_France.xslx'

# Nom du fichier contenant les liens
script_dir = os.path.dirname(__file__)
filenameLinks = 'liens_france.npy'
file_path = os.path.join(script_dir, filenameLinks)



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

n = 0
for i in links :
    n += 1
    try :
        request = requests.get(i, headers = requests_headers, timeout = 10)
        bodyString = request.text
        bodyString = html.unescape(bodyString)
        bodyString = bodyString.replace('\n', '')
        bodyString = bodyString.replace('\t', '')
        bodyString = bodyString.replace('\r', '')
        print(n)

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
        print('lien ', n, ' ne fonctionne pas')
        pass



file_path = os.path.join(script_dir, saveAs)

df = pd.DataFrame.from_dict({'Nom':company,'Email':email,'Adresse':address,'Numéro':number, 'Ville':city, 'Pays':country})
df.to_excel(file_path, header=True, index=False)

