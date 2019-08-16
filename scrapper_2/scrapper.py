import requests
import time
import re
import html
import csv
import os

saveAs = 'Mailing_Avocats_PI_Brevet_Contentieux.csv'

requests_headers = {'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

urlToScrap = 'https://www.magazine-decideurs.com/classements/propriete-industrielle-brevets-contentieux-classement-2019-cabinet-d-avocats-france?locale=fr'

req = requests.get(urlToScrap, headers = requests_headers)
body = req.text
body = html.unescape(body)

numbers = []
offices = []
names = []
jobs = []
emails_lawyer = []
emails_office= []

links = re.findall('<a href="(.+?(?=" target="_blank" class="rankingPlug__rowTeam__name customer"))', body)

for link in links:
    url = 'https:' + link
    request = requests.get(url, headers = requests_headers)
    product = req.text
    contact_list_match = re.search('<ul class="contact-list">(.+?)</ul>', product, flags = re.DOTALL)
    if contact_list_match :
        contact_list = contact_list_match.group(0)
        listItems = re.findall('<li>(.+?)</li>', contact_list, flags = re.DOTALL)

        for li in listItems:
            offices.extend(re.findall('<div class="infos">\n                <h1>(.+?(?=</h1>\n))',product))
            name = re.findall('<span class="name">(.+?(?=</span>\n))', li)
            names.extend(name)
            if '"mailto:' in li :
                email_lawer = re.findall('<a href="mailto:(.+?(?=">))', li)
                emails_lawyer.extend(email_lawer)
            else :
                emails_lawyer.extend('N')

            if 'class="job">' in li :
                job = re.findall('class="job">(.+?(?=</span>\n))', li)
                jobs.extend(job)
            else :
                jobs.extend('N')

result = [names, emails_lawyer, jobs, offices]

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, saveAs)
with open(file_path, "w", encoding = 'utf-8') as outfile :
        data = csv.writer(outfile, delimiter = ';', lineterminator = '\n')
        data.writerow(['Prénom Nom','E-mail','Fonction','Nom du cabinet'])
        for row in zip(*result):
            data.writerow(row)