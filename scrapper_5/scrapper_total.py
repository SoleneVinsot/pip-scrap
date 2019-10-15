import requests
import html
import re
import pandas

from collections import Counter
import pylab

#Importation des listes
import numpy as np

#Modules statistiques
import matplotlib.pyplot as plt
import statistics

#Modules économétrie
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression



########################################################## Avis-Sportifs ###################################################################



#Importation des données d'avis-sportifs avec numpy

cate=[]
cate3=np.load('cate.npy')

marque3=np.load('marque.npy')
nbavis3=np.load('nbavis.npy')
prix3=np.load('prix.npy')
nome=np.load('nom.npy')
nom3=list(nome)

# Calcul du nombre de produits pour chaque marque
cpt3 = Counter(marque3)

#Création des dummies de catégories

dummie_ChaussHomme3=[]
dummie_VêtFemme3=[]
dummie_ChaussFemme3=[]
dummie_Chaussettes3=[]
dummie_Acc3=[]
dummie_SousVet3=[]


for m in cate3 :
    if m =='Chaussures Femme' :
        dummie_ChaussFemme3.append(1)
    else :
        dummie_ChaussFemme3.append(0)

    if m =='Chaussure Homme' :
        dummie_ChaussHomme3.append(1)
    else :
        dummie_ChaussHomme3.append(0)

    if m =='Vêtements Femme' :
        dummie_VêtFemme3.append(1)
    else :
        dummie_VêtFemme3.append(0)

    if m =='Chaussettes et manchons' :
        dummie_Chaussettes3.append(1)
    else :
        dummie_Chaussettes3.append(0)

    if m =='Accessoires' :
        dummie_Acc3.append(1)
    else :
        dummie_Acc3.append(0)

    if m =='Sous-vêtements Homme' or m=='Sous-vêtements Femme':
        dummie_SousVet3.append(1)
    else :
        dummie_SousVet3.append(0)





#Création du data frame
dfA = pandas.DataFrame({'Catégorie': cate3, 'Marque': marque3, 'Prix':prix3, "Nombre d'avis":nbavis3},index = nom3)

i=0
while i<1:
    rep=input('Souhaitez-vous voir les données détaillées des prix et des notes selon les différents produits du site Avis-sportifs ? ')
    if rep=='oui':
        print('Voici le tableau des données du site Avis-sportifs : ')
        print(dfA)
        i=1

    else :
        i=1

####################################################################   DÉCATHLON   ##############################################################


note=[]
nombre_davis=[]
num=[]
nom=[]
marque=[]
prix=[]
px=[]

#liste des pages à scrapper
dic=['C-916521','C-916522','C-916523-vetement-de-course-a-pied/N-714575-genre~homme','C-916523-vetement-de-course-a-pied/N-714575-genre~femme','C-931152','C-931151','C-933425','C-931040']

for e in dic :
    url="https://www.decathlon.fr/"+str(e)
    code=requests.get(url)
    code=code.text
    code=html.unescape(code)
    code=code.replace('\n', '')
    code=code.replace('\t', '')
    code=code.replace('\r','')


    #Code expression du nom du produit :              <h3 class="product-label">CHAUSSURE JOGGING HOMME RUN ONE GRIS</h3>                <div class="rating-container">
    #Le nom du produit
    pattern2='class="product-label">(.+?(?=</h3>                <div class="rating-container">))'
    name=re.findall(pattern2,code)
    nom=nom+name
    for u in name :
        num.append(e)


    #La marque
    #Code expression de la marque :           <h3 class="product-brand">KALENJI</h3>\r\n

    pattern4='data-product-brandname="(.+?(?="    data-product-imgurl))'
    marques=re.findall(pattern4,code)
    marque=marque+marques

    #Le prix
    #Expression euro ='        <div class="price">\r\n(.+?(?=<span))'
    #Expression decimal prix ='<span class=\'decimalSeparator\'>,</span><span class=\'cent\'>(.+?(?=</span><span class))'

    #Probleme texte entre euro et decimal donc remplacement par une virgule
    code=code.replace("<span class=\'decimalSeparator\'>,</span><span class=\'cent\'>",',')
    code=code.replace("<span class=\'decimalSeparator\'></span><span class=\'cent\'>",'')

    pattern1='<div class="price">(.+?(?=</span><span class))'
    price=re.findall(pattern1,code)
    px=px+price

    #Le nombre d'avis
    #Code expression du nombre d'avis :                      <div class="product-rating-number">\r\n(335)\r\n                        </div>\r\n

    #PB : certains produits sans note donc pattern6 pour une boucle avec : si le produit est dans le pattern le prendre sinon mettre un zero
    code=code.replace('(','')
    code=code.replace(')','')

    pattern6='"product-label">(.+?(?=<div class="compare-container">))'
    texte=re.findall(pattern6,code)
    for ele in texte :
        i=['0']
        pattern3='<div class="product-rating-number">                            (.+?(?=                        </div>))'
        if 'product-rating-number' not in ele:
            nombre_davis=nombre_davis+i
        else :
            nb=re.findall(pattern3,ele)
            nombre_davis=nombre_davis+nb


# Compter le nombre de produit pour chaque marque
cpt = Counter(marque)

# Transformer le prix de string à float
for i in px:
    i=i.replace(',','.')
    prix.append(float(i))

# Mettre les bons termes pour le nom de catégorie
cate=[]
for j in num :
    j=j.replace('C-916521','Chaussures Homme')
    j=j.replace('C-916522','Chaussures Femme')
    j=j.replace('C-916523-vetement-de-course-a-pied/N-714575-genre~homme','Vêtements Homme')
    j=j.replace('C-916523-vetement-de-course-a-pied/N-714575-genre~femme','Vêtements Femme')
    j=j.replace('C-931152','Chaussettes et manchons')
    j=j.replace('C-931151','Culottes et boxers')
    j=j.replace('C-933425','Brassières')
    j=j.replace('C-931040','Accessoires')
    cate.append(j)

#Création de dummies de catégories

dummie_ChaussHomme=[]
dummie_VêtFemme=[]
dummie_ChaussFemme=[]
dummie_Chaussettes=[]
dummie_Acc=[]
dummie_SousVet=[]

for n in cate :
    if n =='Chaussures Femme' :
        dummie_ChaussFemme.append(1)
    else :
        dummie_ChaussFemme.append(0)

    if n =='Chaussures Homme' :
        dummie_ChaussHomme.append(1)
    else :
        dummie_ChaussHomme.append(0)

    if n =='Vêtements Femme' :
        dummie_VêtFemme.append(1)
    else :
        dummie_VêtFemme.append(0)

    if n =='Chaussettes et manchons' :
        dummie_Chaussettes.append(1)
    else :
        dummie_Chaussettes.append(0)

    if n =='Accessoires' :
        dummie_Acc.append(1)
    else :
        dummie_Acc.append(0)

    if n =='Culottes et boxers' or n=='Brassières':
        dummie_SousVet.append(1)
    else :
        dummie_SousVet.append(0)



#Transformer le nombre d'avis de string à int
nbavis=[]
for k in nombre_davis :
    nbavis.append(int(k))


#Création d'un data frame
df = pandas.DataFrame({'Catégorie': cate, 'Marque': marque, 'Prix':prix, "Nombre d'avis":nbavis},index = nom)

# Choix pour faire apparaitre le data frame
i=0
while i<1:
    rep=input('Souhaitez-vous voir les données détaillées des prix et des notes selon les différents produits du site Décathlon ? ')
    if rep=='oui':
        print('Voici le tableau des données du site Décathlon : ')
        print(df)
        i=1

    else :
        i=1




####################################################################   GO SPORT   ##############################################################


nom2=[]
num2=[]
marque2=[]
px2=[]
nombre_davis2=[]

#Liste des sites à scrapper
dic=['chaussures/homme/','chaussures/femme/','vetements/homme/','vetements/femme/','accessoires/chaussettes/','vetements/femme/brassieres-running-femme/','accessoires/']

for e in dic :
    url="https://www.go-sport.com/running/"+str(e)
    code2=requests.get(url)
    code2=code2.text
    code2=html.unescape(code2)
    code2=code2.replace('\n', '')
    code2=code2.replace('\t', '')
    code2=code2.replace('\r','')


    #Le nom du produit
    #Code expression nom du produit : <span class="product__category">running RUN 100 M</span>
    patterna='<span class="product__category">(.+?(?=</span>))'
    name2=re.findall(patterna,code2)
    nom2=nom2+name2
    for u in name2 :
        num2.append(e)

    #la marque
    #Code expression marque : <span class="product__title">1ER PRIX</span>

    patternb='<span class="product__title">(.+?(?=</span>))'

    marques2=re.findall(patternb,code2)
    marque2=marque2+marques2

    #Le prix
    #Probleme : parfois <small> dans l'expression donc remplacement par ''
    code2=code2.replace('<small>','')
    asupp=[]
    patt='<span class="price-current" id="product-price-(.+?(?=">))'
    asup=re.findall(patt,code2)
    asupp=asupp+asup
    for l in asupp:
        code2=code2.replace(l,'')

    # Correction de certaines expression qui sont différentes
    code2=code2.replace('                                              ','')
    code2=code2.replace('2576','')
    code2=code2.replace('660','')
    code2=code2.replace('661','')
    patternc='id="product-price-">(.+?(?=\xa0€</small>))'
    price2=re.findall(patternc,code2)
    px2=px2+price2


    #Le nombre d'avis
    #Code expression nombre davis:                      <div class="product-rating-number">\r\n(335)\r\n                        </div>\r\n

    #PB : certains produits sans nombre d'avis donc patternd comme dans le code de Décathlon

    patternd='class="product__title">(.+?(?=Vendu et expédié par))'
    texte2=re.findall(patternd,code2)
    for ele in texte2 :
        i=['0']
        patterne='<span class="review__number">(.+?(?= avis</span></a>))'
        if '"review__number"' not in ele:
            nombre_davis2=nombre_davis2+i
        else :
            nb2=re.findall(patterne,ele)
            nombre_davis2=nombre_davis2+nb2
# Nombre de fois ou apparrait le nom de chaque marque => nombre de produit pour chaque marque
cpt2 = Counter(marque2)

# Transformation du nombre d'avis de string à int
nbavis2=[]
for k in nombre_davis2 :
    nbavis2.append(int(k))
#Transformation du prix de string à float
prix2=[]
for i in px2:
    i=i.replace(',','.')
    i=i.replace(' ','')
    prix2.append(float(i))


# Mettre les bons termes pour le nom de catégorie
cate2=[]
for j in num2 :
    j=j.replace('chaussures/homme/','Chaussure Homme')
    j=j.replace('chaussures/femme/','Chaussures Femme')
    j=j.replace('vetements/homme/','Vêtements Homme')
    j=j.replace('vetements/femme/','Vêtements Femme')
    j=j.replace('accessoires/chaussettes/','Chaussettes et manchons')
    j=j.replace('Vêtements Femmebrassieres-running-femme/','Brassières')
    j=j.replace('accessoires/','Accessoires')
    cate2.append(j)


#Création de dummies de catégories
dummie_ChaussHomme2=[]
dummie_VêtFemme2=[]
dummie_ChaussFemme2=[]
dummie_Chaussettes2=[]
dummie_Acc2=[]
dummie_SousVet2=[]

for o in cate2 :
    if o =='Chaussures Femme' :
        dummie_ChaussFemme2.append(1)
    else :
        dummie_ChaussFemme2.append(0)

    if o =='Chaussure Homme' :
        dummie_ChaussHomme2.append(1)
    else :
        dummie_ChaussHomme2.append(0)

    if o =='Vêtements Femme' :
        dummie_VêtFemme2.append(1)
    else :
        dummie_VêtFemme2.append(0)

    if o =='Chaussettes et manchons' :
        dummie_Chaussettes2.append(1)
    else :
        dummie_Chaussettes2.append(0)

    if o =='Accessoires' :
        dummie_Acc2.append(1)
    else :
        dummie_Acc2.append(0)

    if o =='Brassières':
        dummie_SousVet2.append(1)
    else :
        dummie_SousVet2.append(0)

# Création d'un dat frame
df2 = pandas.DataFrame({'Catégorie': cate2, 'Marque': marque2, 'Prix':prix2, "Nombre d'avis":nbavis2},index = nom2)

# Choix pour faire apparaitre le data frame
j=0
while j<1:
    rep=input('Souhaitez-vous voir les données détaillées des prix et des notes selon les différents produits du site Go Sport ? ')
    if rep=='oui':
        print('Voici le tableau des données du site Go Sport : ')
        print(df2)
        j=1
    else :
        j=1







############################################################### STATISTIQUES ########################################################################

# Analyse statistique des variables prix de chaque site
Décathlon=[statistics.mean(prix),statistics.median(prix),statistics.variance(prix)]
Go_Sport=[statistics.mean(prix2),statistics.median(prix2),statistics.variance(prix2)]
Avis_sportifs=[statistics.mean(prix3),statistics.median(prix3),statistics.variance(prix3)]
#Création d'un data frame
Stat=['Moyenne','Médiane','Variance']
df3 = pandas.DataFrame({'Décathon': Décathlon , 'Go Sport': Go_Sport, 'Avis-sportifs':Avis_sportifs},index = Stat)

# Analyse statistique des variables nombre d'avis de chaque site
Décathlon1=[statistics.mean(nbavis),statistics.median(nbavis),statistics.variance(nbavis)]
Go_Sport1=[statistics.mean(nbavis2),statistics.median(nbavis2),statistics.variance(nbavis2)]
Avis_sportifs1=[statistics.mean(nbavis3),statistics.median(nbavis3),statistics.variance(nbavis3)]
#Création d'un data frame
Stat1=['Moyenne','Médiane','Variance']
df4 = pandas.DataFrame({'Décathon': Décathlon1 , 'Go Sport': Go_Sport1, 'Avis-sportifs':Avis_sportifs1},index = Stat1)

#Choix de faire apparaitre les deux data frame
l=0
while l<1:
    rep=input('Souhaitez-vous voir les statistiques des différents sites ? ')
    if rep=='oui':
        print('Voici le tableau des statistiques des prix des différents sites : ')
        print(df3)
        print('Voici le tableau des statistiques des nombres d avis des différents sites : ')
        print(df4)
        l=1
    else :
        l=1




############################################################### Graphiques ########################################################################

#comparaison des distributions de prix avec un pyplot de matplotlib

#Histogramme Distribution_des_prix
x1 =prix3
x2 = prix
x3=prix2
n, bins, patches =plt.hist([x1, x2,x3], bins = 5, color = ['blue', 'red','green'],edgecolor = 'grey', label = ['Décathlon', 'Go Sport','Avis-sportifs'])
plt.ylabel('nombres')
plt.xlabel('prix')
plt.title('Distribution des prix')
plt.savefig('Distribution_des_prix.png')

#Histogramme Distribution_des_nombres_davis
x1 =nbavis3
x2 = nbavis
x3=nbavis2
n, bins, patches =plt.hist([x1, x2,x3], bins = 10, color = ['blue', 'red','green'],edgecolor = 'grey', label = ['Décathlon', 'Go Sport','Avis-sportifs'])
plt.xlim(0,300)
plt.ylabel('nombres')
plt.xlabel('nombre d avis')
plt.title('Distribution des nombres d avis')
plt.savefig('Distribution_des_nombres_davis.png')





#Boites_à_moustaches_prix
x1 =prix3
x2 = prix2
x3=prix

BoxName = ['Avis-sportifs','Décathlon','Go Sport']
data = [x1, x2,x3]
plt.boxplot(data)
pylab.xticks([1,2,3], BoxName)
plt.title('Distribution des prix')
plt.ylabel('prix')
plt.savefig('Boites_à_moustaches_prix.png')


#Boites_à_moustaches_nombres_davis
x1 =nbavis3
x2 = nbavis
x3=nbavis2

BoxName2 = ['Avis-sportifs','Décathlon','Go Sport']
data = [x1, x2,x3]
plt.boxplot(data)
plt.ylim(0,300)
pylab.xticks([1,2,3], BoxName2)
plt.title('Distribution des nombres d avis')
plt.ylabel("nombre d'avis")
plt.savefig('Boites_à_moustaches_nombres_davis.png')


############################################################### Création de dummies ###############################################################

#Dummies des différentes categorie pour les 3 sites
d_ChaussHomme=dummie_ChaussHomme3+dummie_ChaussHomme+dummie_ChaussHomme2
d_VêtFemme=dummie_VêtFemme3+dummie_VêtFemme+dummie_VêtFemme2
d_ChaussFemme=dummie_ChaussFemme3+dummie_ChaussFemme+dummie_ChaussFemme2
d_Chaussettes=dummie_Chaussettes3+dummie_Chaussettes+dummie_Chaussettes2
d_Acc=dummie_Acc3+dummie_Acc+dummie_Acc2
d_SousVet=dummie_SousVet3+dummie_SousVet+dummie_SousVet2

#prix des 3 sites
prix_total=list(prix3)
prix_total.extend(prix)
prix_total.extend(prix2)

#nombre davis des 3 sites
nombre_davis_total=list(nbavis3)
nombre_davis_total.extend(nbavis)
nombre_davis_total.extend(nbavis2)

#nom des produits des 3 sites
nom_produit_total=list(nom3)
nom_produit_total.extend(nom)
nom_produit_total.extend(nom2)

#############################################################################  Dummies site ################################################################################

dummieAS=[]

for ele in prix3 :
    dummieAS.append('1')

for ele in prix :
    dummieAS.append('0')

for ele in prix2 :
    dummieAS.append('0')

dummieD=[]

for ele in prix3 :
    dummieD.append('0')

for ele in prix :
    dummieD.append('1')

for ele in prix2 :
    dummieD.append('0')

dummieGS=[]

for ele in prix3 :
    dummieGS.append('0')

for ele in prix :
    dummieGS.append('0')

for ele in prix2 :
    dummieGS.append('1')

############################################################### Econométrie modèle total avec dummies catégories ###############################################################
print('L’analyse prenant en compte la catégorie de produit')

#Reference de la régression linéaire : vetements homme

dfB = pandas.DataFrame({'nombre_davis_total':nombre_davis_total,'prix_total':prix_total,'dummie_ChaussHomme': d_ChaussHomme,'dummie_ChaussFemme':d_ChaussFemme, 'dummie_VêtFemme': d_VêtFemme, 'dummie_Chaussettes':d_Chaussettes,'dummie_SousVet':d_SousVet,'dummie_Accessoires':d_Acc},index = nom_produit_total)


#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X présents dans le dat frame
list_var=dfB.columns.drop("nombre_davis_total")
y=dfB.nombre_davis_total
X=dfB[list_var]

modeleReg.fit(X,y)

print("La prédiction du nombre d'avis d'un produit de la catégorie vetements homme sans prendre en compte le prix est de  ",modeleReg.intercept_)
print("Les facteurs des différentes variables du modèle 1 sont : ",modeleReg.coef_)

#Prédictions du modèles
RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

#Nous obtenons deux graphiques représentant :
#Les valeurs de y en fonction des valeurs prédites avec le modèle de régresssion linéaire
plt.plot(y, modeleReg.predict(X),'.')
#Les valeurs de Y en fonction des résidus
plt.plot(y, y-modeleReg.predict(X),'.')


print('Voici les résultats de la régression linéaire du modèle total avec les dummies de catégories')
reg = smf.ols('nombre_davis_total ~ prix_total+d_ChaussHomme+d_ChaussFemme+ d_VêtFemme+d_Chaussettes+d_SousVet+d_Acc', data = dfB)
res=reg.fit()
print(res.summary())

############################################################### Econométrie modèle total avec dummies marque ###############################################################
print("L’analyse prenant en compte la marque du produit")
#Reference autres marques

print('Voici le décompte des produits selon la marque du site Avis-sportifs ',cpt3)
print('Voici le décompte des produits selon la marque du site Décathlon ',cpt)
print('Voici le décompte des produits selon la marque du site Go Sport ',cpt2)

print('Les marques les plus présentes sont : Kalenji, Asics, Mizuno, Nike, Adidas et Athlitech.  On va donc faire des dummies pour ces marques pour analyser l impact de la marque sur le nombre d avis')

marque_total=list(marque3)
marque_total.extend(marque)
marque_total.extend(marque2)

dummie_KALENJI=[]
dummie_ASICS=[]
dummie_MIZUNO=[]
dummie_ADIDAS=[]
dummie_NIKE=[]
dummie_ATHLITECH=[]

for p in marque_total :

    if p=='KALENJI' :
        dummie_KALENJI.append(1)
    else :
        dummie_KALENJI.append(0)

    if p=='Asics' or p=='ASICS' :
        dummie_ASICS.append(1)
    else :
        dummie_ASICS.append(0)

    if p=='MIZUNO' or p=='Mizuno' :
        dummie_MIZUNO.append(1)
    else :
        dummie_MIZUNO.append(0)

    if p=='ADIDAS' or p=='Adidas' :
        dummie_ADIDAS.append(1)
    else :
        dummie_ADIDAS.append(0)

    if p=='Nike' or p=='NIKE' :
        dummie_NIKE.append(1)
    else :
        dummie_NIKE.append(0)

    if p=='ATHLI-TECH' or p=='ATHLITECH' :
        dummie_ATHLITECH.append(1)
    else :
        dummie_ATHLITECH.append(0)

# Création d'un data frame
dfC = pandas.DataFrame({'nombre_davis_total':nombre_davis_total,'prix_total':prix_total,'dummie_KALENJI': dummie_KALENJI,'dummie_ASICS':dummie_ASICS, 'dummie_MIZUNO': dummie_MIZUNO, 'dummie_ADIDAS':dummie_ADIDAS,'dummie_NIKE':dummie_NIKE,'dummie_ATHLITECH':dummie_ATHLITECH},index = nom_produit_total)


#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X
list_var=dfC.columns.drop("nombre_davis_total")
y=dfC.nombre_davis_total
X=dfC[list_var]

modeleReg.fit(X,y)

print("La prédiction du nombre d'avis d'un produit est de  ",modeleReg.intercept_)
print("Les facteurs des différentes variables du modèle 2 sont : ",modeleReg.coef_)




RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

#Nous obtenons deux graphiques (qu’il faudrait mieux préparer) représentant : les valeurs de y en fonction des valeurs prédites avec le modèle de régresssion linéaire et les valeurs de Y en fonction des résidus
plt.plot(y, modeleReg.predict(X),'.')
plt.plot(y, y-modeleReg.predict(X),'.')


print('Voici les résultats de la régression linéaire du modèle total avec les dummies de marques')
reg = smf.ols('nombre_davis_total ~ prix_total+dummie_KALENJI+dummie_ASICS+dummie_MIZUNO+dummie_ADIDAS+dummie_NIKE+dummie_ATHLITECH', data = dfC)
res=reg.fit()
print(res.summary())

############################################################### Econométrie modèle total  ###############################################################

print("L’analyse prenant en compte la totalité des variables")
#ref avis-sportifs
dfD = pandas.DataFrame({'nombre_davis_total':nombre_davis_total,'prix_total':prix_total,'dummie_KALENJI': dummie_KALENJI,'dummie_ASICS':dummie_ASICS, 'dummie_MIZUNO': dummie_MIZUNO, 'dummie_ADIDAS':dummie_ADIDAS,'dummie_NIKE':dummie_NIKE,'dummie_ATHLITECH':dummie_ATHLITECH,'dummie_ChaussHomme': d_ChaussHomme,'dummie_ChaussFemme':d_ChaussFemme, 'dummie_VêtFemme': d_VêtFemme, 'dummie_Chaussettes':d_Chaussettes,'dummie_SousVet':d_SousVet,'dummie_Accessoires':d_Acc,'dummieD':dummieD,'dummieGS':dummieGS},index = nom_produit_total)


#créer un objet reg lin
modeleReg=LinearRegression()

#créer y et X
list_var=dfD.columns.drop("nombre_davis_total")
y=dfD.nombre_davis_total
X=dfD[list_var]

modeleReg.fit(X,y)

print("La prédiction du nombre d'avis d'un produit est de  ",modeleReg.intercept_)
print("Les facteurs des différentes variables du modèle 2 sont : ",modeleReg.coef_)




RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))
#Nous obtenons deux graphiques (qu’il faudrait mieux préparer) représentant : les valeurs de y en fonction des valeurs prédites avec le modèle de régresssion linéaire et les valeurs de Y en fonction des résidus
plt.plot(y, modeleReg.predict(X),'.')
plt.plot(y, y-modeleReg.predict(X),'.')



print('Voici les résultats de la régression linéaire du modèle total contenant la totalité des variables')
reg = smf.ols('nombre_davis_total ~ prix_total+dummie_KALENJI+dummie_ASICS+dummie_MIZUNO+dummie_ADIDAS+dummie_NIKE+dummie_ATHLITECH+d_ChaussHomme+d_ChaussFemme+ d_VêtFemme+d_Chaussettes+d_SousVet+d_Acc+dummieD+dummieGS', data = dfD)
res=reg.fit()
print(res.summary())





#################################################### ENREGISTREMENT SOUS EXCEL ########################################################################

k=0
while k<1:
    rep=input('Souhaitez-vous avoir la version excel des données détaillées ainsi que des statisques des prix et des notes selon les différents produits des trois sites ? ')
    if rep=='oui':
        writer = pandas.ExcelWriter('output.xlsx')
        dfA.to_excel(writer,'Avis-sportifs')
        df.to_excel(writer,'Décathlon')
        df2.to_excel(writer,'Go Sport')
        df3.to_excel(writer,"Stat Prix")
        df4.to_excel(writer,"Stat Nombre d'avis")
        writer.save()
        k=1

    else :
        k=1


