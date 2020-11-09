import matplotlib.pyplot as plt
import json
from collections import Counter
import pdb
import numpy as np
import statistics


with open('base_totale.json','r') as onput :
  base=json.load(onput)



#Nombre de produit par marque
marque=[]
marques=[]
nb_prod=[]

for ele in base["Produits sans avis"] :
  marque.append(ele['Marque'][0])

count_marque=Counter(marque)
#Résultat du counter : Counter({'Trek': 36, 'Cervelo': 9, 'Felt': 9, 'Heroïn': 8, 'Cube': 6, 'Sunn': 3, 'BH': 1, 'Focus': 1})
count_marque=dict(count_marque)

for e in count_marque :
  marques.append(e)
for e in marques :
  nb_prod.append(count_marque[e])

plt.bar(marques,nb_prod)
plt.title("Représentation graphique du nombre de produits par marque")
plt.xlabel("Marque")
plt.ylabel("Nombre de produits")
plt.legend()
plt.savefig("marque.png")
plt.close()

#Répartition des prix

prix=[]

for ele in base["Produits sans avis"] :
  prix.append(float(ele['Prix'][0]))

print("Le prix maximal est de :            ",max(prix))
print("Le prix maximal est de :            ",min(prix))
print("La médiane des prix est de :        ",np.median(np.array(prix)))
print("La moyenne des prix est de :        ",statistics.mean(prix))



plt.boxplot(prix)
plt.title("Représentation graphique de la répartition des prix")
plt.savefig("prix.png")
plt.close()
#Répartition des genres
#Pas d'intérêt à recommander selon le sexe

genre=[]
genres=[]
nb_genre=[]
genre_p=[]

for ele in base["Produits sans avis"] :
  genre.append(ele['Genre'])

for i in genre :
  if i =="Men<br>Women":
    i=i.replace("Men<br>Women","Neutre")
    genre_p.append(i)
  elif i=="Women<br>Men":
    i=i.replace("Women<br>Men","Neutre")
    genre_p.append(i)
  else :
    genre_p.append(i)


count_genre=Counter(genre_p)
#Résultat du counter : Counter({'Men': 56, 'Women': 6, 'Neutre': 11})
count_genre=dict(count_genre)

for e in count_genre :
  genres.append(e)
for e in genres :
  nb_genre.append(count_genre[e])

plt.pie(nb_genre, labels = genres, colors = ['deepskyblue', 'dodgerblue', 'steelblue'])
plt.title("Représentation du genre des différents produits")
plt.savefig("genre.png")
plt.close()
#Groupe de transmission

groupe=[]
groupes=[]
nb_groupe=[]

for ele in base["Produits sans avis"] :
  groupe.append(ele['Groupe'])

count_groupe=Counter(groupe)
#Résultat du counter : Counter({'Men': 56, 'Women': 6, 'Neutre': 11})
count_groupe=dict(count_groupe)

for e in count_groupe :
  groupes.append(e)
for e in groupes :
  nb_groupe.append(count_groupe[e])

plt.barh(groupes, nb_groupe)
plt.title("Représentation graphique du nombre de produits selon le groupe de transmission")
plt.legend()
plt.savefig("groupe.png")
plt.show()
plt.close()

pdb.set_trace()

