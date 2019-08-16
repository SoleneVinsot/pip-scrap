import time
import re
import requests
import html
import csv
import numpy as np
import os

# Nom du fichier contenant les liens
filenameLinks = 'liens_france.npy'

# Nom du fichier de sauvegarde
saveAs = 'contacts_avocats_barreau_paris.csv'

linksObject = np.load(filenameLinks)
# Transforme notre object en liste
links = list(linksObject)

# Ces liens ne fonctionnent pas
del links[281]
del links[575]
del links[625]
del links[454]

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

result = [company, email, address, city, country , number]

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, saveAs)
with open(file_path, "w", encoding = 'utf-8') as outfile :
    data = csv.writer(outfile, delimiter = ';', lineterminator = '\n')
    data.writerow(['Nom', 'Email', 'Adresse', 'Ville', 'Pays', 'Numéro'])
    for row in zip(*result) :
        data.writerow(row)