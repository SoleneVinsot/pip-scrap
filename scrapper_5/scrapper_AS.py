# -*- coding: utf8 -*-
import re
import requests
import time
import pdb
import os
import html
import csv
import matplotlib.pyplot as plt
import statistics
import numpy as np



price=[]
prix=[]
nombre_davis=[]
num=[]
nbavis=[]
marques=[]
marque=[]
nom2=[]



total=str()

dic2=['4735-chaussures-running-homme','4736-chaussures-running-femme','4748-vetements-running-homme','4749-vetements-running-femme','4213-chaussettes-et-manchons-running','4743-sous-vetements-running-homme','4744-sous-vetements-running-femme','4214-accessoires-running']

for p in dic2:
    url='https://www.avis-sportifs.com/'+str(p)
    req=requests.get(url)
    contenu=req.text




    #La marque
    pattern4='display: inline-block;">(.+?(?=</span>            <span))'
    marque=re.findall(pattern4,contenu)
    marques=marques+marque

    for u in marque :
            num.append(p)

    #page de chaque produit
    pattern='<a href="(.+?(?=" class="thumbnail product-thumbnail">\n))'
    result=re.findall(pattern,contenu)

    for e in result:
        req=requests.get(e)
        produit=req.text

        #Le nom du produit
        patternD='                   <span itemprop="name">(.+?(?=</span>))'
        name2=re.findall(patternD,produit)
        nom2=nom2+name2


        #prix
        pattern1='<meta itemprop="price" content="(.+?(?=\xa0">\n))'
        px=re.findall(pattern1,produit)
        price=price+px

        i=['0']


        #nombre d'avis
        pattern3='md-nb-avis" itemprop="reviewCount">&nbsp;(.+?(?=</span><span class))'
        if 'md-nb-avis' not in produit:
            nombre_davis=i+nombre_davis
        else :
            nb=re.findall(pattern3,produit)
            nombre_davis=nb+nombre_davis




cate=[]
for j in num:
    j=j.replace('4735-chaussures-running-homme','Chaussure Homme')
    j=j.replace('4736-chaussures-running-femme','Chaussures Femme')
    j=j.replace('4748-vetements-running-homme','Vêtements Homme')
    j=j.replace('4749-vetements-running-femme','Vêtements Femme')
    j=j.replace('4213-chaussettes-et-manchons-running','Chaussettes et manchons')
    j=j.replace('4744-sous-vetements-running-femme','Sous-vêtements Femme')
    j=j.replace('4743-sous-vetements-running-homme','Sous-vêtements Homme')
    j=j.replace('4214-accessoires-running','Accessoires')
    cate.append(j)

for t in price:
        t=float(t)
        prix.append(t)

for q in nombre_davis :
        q=float(q)
        nbavis.append(q)

#sauvegarde des listes avec numpy
np.save('nbavis',nbavis)
np.save('prix',prix)
np.save('cate',cate)
np.save('marque',marques)
np.save('nom',nom2)






