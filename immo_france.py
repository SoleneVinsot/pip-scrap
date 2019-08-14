import time
import re
import requests
import html
import csv
import numpy as np

liens=np.load("liens_france.npy")
liens=list(liens)

requests_headers={'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

adresse=[]
city=[]
pays=[]
numero=[]
entreprise=[]
email=[]

del liens[281]
del liens[575]
del liens[625]
del liens [454]
print(liens)

total_link = 0
## Pour chaque
##
##
##
##
for i in liens :
  n += 1
  req=requests.get(i, headers=requests_headers, timeout=10)
  code=req.text
  code=html.unescape(code)
  code=code.replace('\n', '')
  code=code.replace('\t', '')
  code=code.replace('\r','')
  #entreprise
  pat1='<span itemprop="itemreviewed" ><em>(.+?(?=</em></span>))'
  ent=re.findall(pat1,code)
  entreprise.extend(ent)




    #adresse et numéro
    pat2='</div><div class="Information"><span>(.+?(?=</span></div>))'
    ad=re.findall(pat2,code)

    adresse.append(ad[0])
    city.append(ad[1])
    pays.append(ad[2])
    numero.append(ad[3])

    #mail
    pat3='E-mail</span></div><div class="Colon"><span>:</span></div><div class="Information"><a href="mailto:(.+?(?=">))'
    mail=re.findall(pat3,code)
    email.extend(mail)

print(len(entreprise))
print(len(adresse))
print(len(city))
print(len(pays))
print(len(numero))
print(len(email))

K=[entreprise,email,adresse,city,pays,numero]
with open("contacts_avocats_barreau_paris.csv", "w",encoding='utf-8') as outfile:
        data=csv.writer(outfile,delimiter=';',lineterminator='\n')
        data.writerow(['Nom','Email','Adresse','Ville','Pays','Numéro'])
        for row in zip(*K):
            data.writerow(row)