import numpy as np
import requests
import re
import pdb
import html
import json

#######################sur Alltricks###################
#Problème produits anciens donc ils n'ont pas de genre ni année ni groupe + liens ne fonctionnent pas tous
liens=np.load("liens_Avis_ALL.npy")
liens=list(liens)

descriptions=[]
id=[]
marques=[]
prix=[]
genre=[]
groupe=[]
annee=[]
tot=[]

#liste des liens (Avis-Sportifs) qui sont toujours visibles sur Alltricks
liste_liens_avis=['/F-41505-velos-route---cyclocross---triathlon/P-684752-velo-de-route-trek-madone-sl-6-shimano-ultegra-11v-2019-rouge---blanc','/F-41505-velos-route---cyclocross---triathlon/P-507371-gravel-bike-cinelli-zydeco-sram-apex-11v-2019-noir---argent---multi-couleur','/F-41505-velos-route---cyclocross---triathlon/P-344935-gravel-bike-kona-rove-shimano-claris-8v-2018-marron']

for ele in liste_liens_avis :
  url='https://www.alltricks.com'+ele
  req=requests.get(url)
  code = req.text
  code = html.unescape(code)
  code = code.replace('\n', '')
  code = code.replace('\t', '')
  code = code.replace('\r','')

  #Nom du produit
  pat1='"name":"(.+?(?=",))'
  description=re.findall(pat1,code)
  descriptions.extend(description)

  #Identifiant du produit
  pat2='{"product":{"id":(.+?(?=,))'
  identifiant=re.findall(pat2,code)
  id.extend(identifiant)

  #Marque du produit
  pat3='"brand":"(.+?(?=",))'
  marque=re.findall(pat3,code)
  marques.extend(marque)

  #Prix du produit
  pat4='"price":"(.+?(?=",))'
  px=re.findall(pat4,code)
  prix.extend(px)



##############Avis-sportifs##############

#liste des liens (Alltricks) dont on a extrait les avis
liste_liens_avis=['/148616-velo-de-route-trek-madone-sl-6-shimano-ultegra-11v-2019-rouge-blanc-601842042564.html','/148618-gravel-bike-cinelli-zydeco-sram-apex-11v-2019-noir-argent-multi-couleur-8058774827103.html','/70851-gravel-bike-kona-rove-shimano-claris-8v-2018-marron-841073120222.html']

url='https://www.avis-sportifs.com'
notes=[]
produits_avec_avis=[]
n=0
for ele in liste_liens_avis:

  req=requests.get(url+ele)
  code = req.text
  code = html.unescape(code)
  code = code.replace('\n', '')
  code = code.replace('\t', '')
  code = code.replace('\r','')

  #Nombre d'avis
  pat1='<span class="md-nb-avis" itemprop="reviewCount">\xa0(.+?(?=</span><span))'
  nombre_avis=re.findall(pat1,code)

  #Note
  pat2='<span class="md_global_rate_number" itemprop="ratingValue">(.+?(?=</span> ))'
  notes=re.findall(pat2,code)

  #Titre avis
  pat3='700;line-height: 2.7;">\xa0«(.+?(?=»</span><p))'
  titre=re.findall(pat3,code)

  #sous titre
  pat4='class="md-avis-text">(.+?(?=<))'
  sous_titre=re.findall(pat4,code)

  #total
  pat5='<span class="md-avantages">(.+?(?=</span>))'
  total=re.findall(pat5,code)
  #Positif
  positif=total[0]
  #Négatif
  negatif=total[1]
  #Rapport qualité_prix
  pat6='class="md-avantages"> Rapport Qualité Prix : (.+?(?=</span>))'
  rapport=re.findall(pat6,code)

  #note de l'avis
  pat7='<div class="comment_grade">(.+?(?=</div></div><span))'
  note_indiv=re.findall(pat7,code)

  #Construction des dictionnaires nécessaire à la base Json
  if len(titre)>1:

    Avis_n1={"Titre":titre[0],"Notation":note_indiv[0],"Sous_titre":sous_titre[0],"Positif":positif[0],"Négatif":negatif[0],"Rapport qualité_prix":rapport[0]}
    Avis_n2={"Titre":titre[1],"Notation":note_indiv[1],"Sous_titre":sous_titre[1],"Positif":positif[1],"Négatif":negatif[1],"Rapport qualité_prix":rapport[1]}
    détail={"Avis n1":Avis_n1, "Avis n2":Avis_n2}
  else :

    Avis_n1={"Titre":titre,"Notation":note_indiv,"Sous_titre":sous_titre,"Positif":positif,"Négatif":negatif,"Rapport qualité_prix":rapport}
    détail={"Avis n1":Avis_n1}


  idn=id[n]
  descriptionn=descriptions[n]
  marquen=marques[n]
  prixn=prix[n]



  Avis={"Nombre d'avis":nombre_avis,"Notation":notes,"détail":détail}
  Produits={'Nom':descriptionn,'ID':idn,'Marque':marquen,'Prix':prixn,"Avis":Avis}


  produits_avec_avis.append(Produits)
  n=n+1

#Chargement de la base de départ
with open('base_alltricks.json','r') as input :
  base=json.load(input)

#Fusion des deux bases
totalite={"Produits avec avis":produits_avec_avis,"Produits sans avis":base}

#Enregistrement de la base comprenant la totalité des informations
with open ("base_totale.json",'w') as output:
  json.dump(totalite,output)
