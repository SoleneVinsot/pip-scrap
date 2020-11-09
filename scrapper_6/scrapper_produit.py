import requests
import numpy as np
import pdb
import html
import re
import json

#Importer les liens produits alltricks
liens=np.load("liens.npy")


produits_avec_avis=[]
n=0

#Boucle pour prendre chaque produit un par un
for ele in liens :
  url='https://www.alltricks.com/'+ele
  req=requests.get(url)
  code = req.text
  code = html.unescape(code)
  code = code.replace('\n', '')
  code = code.replace('\t', '')
  code = code.replace('\r','')

  #Nom du produit
  pat1='"name":"(.+?(?=",))'
  descriptions=re.findall(pat1,code)

  #Identifiant du produit
  pat2='{"product":{"id":(.+?(?=,))'
  id=re.findall(pat2,code)


  #Marque du produit
  pat3='"brand":"(.+?(?=",))'
  marques=re.findall(pat3,code)

  #Prix du produit
  pat4='"price":"(.+?(?=",))'
  prix=re.findall(pat4,code)

  #Genre, groupe et année du produit
  pat5='<td class="spec-value">                                                    (.+?(?=                                            </td>))'
  total=re.findall(pat5,code)
  if len(total)>3 :
    del total[0]
    genre=total[0]
    groupe=total[1]
    annee=total[2]
  else :
    genre=total[0]
    groupe=total[1]
    annee=total[2]

  #Dictionnaire produit
  Produits={'Nom':descriptions,'ID':id,'Marque':marques,'Prix':prix,'Genre':genre,"Groupe":groupe,"Année":annee}

  #Liste comprenant la totalité des disctionnaires produit
  produits_avec_avis.append(Produits)
  n=n+1


#Enregistrement de la base de donnée en Json
with open("base_alltricks.json",'w') as output:
  json.dump(produits_avec_avis,output)







