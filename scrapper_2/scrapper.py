import requests
import time
import re
import html
import csv
import os
import pandas as pd

# Nom du fichier de sauvegarde
saveAs = 'Mailing_Avocats_PI_Brevet_Contentieux.xlsx'

# Récupération du path du fichier
script_dir = os.path.dirname(__file__)



# URL à scrapper
urlToScrap = 'https://www.magazine-decideurs.com/classements/propriete-industrielle-brevets-general-classement-2019-cabinet-de-conseils-en-pi-france?locale=fr'




requests_headers = {'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

req = requests.get(urlToScrap, headers = requests_headers)
body = req.text
body = html.unescape(body)

numbers = []
offices = []
names = []
jobs = []
emails_lawyer = []
emails_office = []

links = re.findall('<a href="(.+?(?=" target="_blank" class="rankingPlug__rowTeam__name customer"))', body)


for link in links:
    url = 'https:' + link
    req = requests.get(url, headers = requests_headers)
    product = req.text
    pattern = '<ul class="contact-list">(.+?)</ul>'
    contact_list_match = re.search(pattern, product, flags = re.DOTALL)



    # Si le contact est trouvé
    if contact_list_match :
        contact_list = contact_list_match.group(0)
        listItems = re.findall('<li>(.+?)</li>', contact_list, flags = re.DOTALL)


        for li in listItems:
            offices.extend(re.findall('<div class="infos">\n                <h1>(.+?(?=</h1>\n))',product))
            name = re.findall('<span class="name">(.+?(?=</span>\n))', li)
            names.extend(name)
            if '"mailto:' in li :
                email_lawyer = re.findall('<a href="mailto:(.+?(?=">))', li)
                emails_lawyer.extend(email_lawyer)
            else :
                emails_lawyer.extend('N')

            if 'class="job">' in li :
                job = re.findall('class="job">(.+?(?=</span>\n))', li)
                jobs.extend(job)
            else :
                jobs.extend('N')




df = pd.DataFrame.from_dict({
  'Nom': names,
  'Email': emails_lawyer,
  'Fonction': jobs,
  'Nom du cabinet': offices
})



file_path_save = os.path.join(script_dir, saveAs)
df.to_excel(file_path_save)