import time
import re
import requests
import html
import csv
import re
import requests
import os
import pandas as pd
import openpyxl
import xlsxwriter
#from openpyxl import load_workbook



#saveAs = 'contact_avocats_marseille_essaie.xslx'

requests_headers = {'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}


liste_disciplines = []
liste_fax = []
liste_noms = []
liste_numéros = []
liste_mails = []
adresse = []

n = 0

while n<77:

    url = 'https://www.barreau-marseille.avocat.fr/fr/annuaire/page-'+str(n)+'?&full=&nom=&specialites=&recherche_annuaire-submit=Ok'
    req = requests.get(url, headers=requests_headers, timeout=10)

    code = req.text
    code = html.unescape(code)
    code = code.replace('\n', '')
    code = code.replace('\t', '')
    code = code.replace('\r','')



    pat1 = '<div class="noms">                                <h2>(.+?(?=</h2>))'
    nom = re.findall(pat1,code)
    liste_noms.extend(nom)

    pat_exclusion='<div class="noms">(.+?(?=activité))'
    exclu = re.findall(pat_exclusion,code)
    for e in exclu :
        if 'Droit' in e:
            pat2 = '</div>                                                            <h3>(.+?(?=</h3>))'
            discipline = re.findall(pat2,e)
            liste_disciplines.extend(discipline)
        else :
            liste_disciplines.append('Non indiquée')
        pat4 = '<strong>Tél :</strong>                            (.+?(?=                                                                        <p>))'

        if '<strong>Tél' in e :
            numéro = re.findall(pat4,e)
            liste_numéros.extend(numéro)
        else :
            liste_numéros.append('NA')

        if '<strong>Fax :' in e:
            pat5 = 'Fax :</strong> (.+?(?=<p>))'
            fax = re.findall(pat5,e)
            liste_fax.extend(fax)
        else :
            liste_fax.append('NA')


        if 'mailto:' in e :
            pat6 = '<a href="mailto:(.+?(?=" >))'
            mail = re.findall(pat6,e)
            liste_mails.extend(mail)
        else :
            liste_mails.append('NA')


        if ' - 13' in e :
            regex = '<p>([^<>]*?\\d{4,5}.*?)</p>'
            long = re.findall(regex,e)
            adresse.extend(long)
        else :
            adresse.append('NA')
    n += 1

#test des listes
print(len(adresse))
print(len(liste_noms))
print(len(liste_mails))
print(len(liste_numéros))
print(len(liste_fax))
print(len(liste_disciplines))


# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, saveAs)
df = pd.DataFrame.from_dict({'Nom':liste_noms,'Email':liste_mails,'Adresse':adresse,'Numéro':liste_numéros,'Fax':liste_fax,'Activité':liste_disciplines})
df.to_excel('contact_avocats_marseille.xlsx', header=True, index=False)




