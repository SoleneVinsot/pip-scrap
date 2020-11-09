import json
import pdb



with open('base_totale.json','r') as onput :
  base=json.load(onput)
#pdb.set_trace()
marque_base=['Trek', 'Cervelo', 'Felt', 'Heroïn', 'Cube', 'Sunn', 'BH', 'Focus']
"""pdb.set_trace()"""
print("Pour accéder à la recommandation d'un vélo, veuillez répondre aux questions suivantes.")


budget_min=input('Quel est votre budget minimal ? ')

budget_max = input("Quel est votre budget maximal ? ")
marque_choice = input ("Avez-vous une marque de préférence ?")

budget_min=int(budget_min)
budget_max=int(budget_max)

if marque_choice == 'oui' or marque_choice=='Oui' :
  print("Voici la liste des marques des produits disponibles :   'Trek', 'Cervelo', 'Felt', 'Heroïn', 'Cube', 'Sunn', 'BH', 'Focus'" )
  marque_choisie = input("Quelle marque préferez-vous ?")
else :
  1

############################Première recommandation##############################
Prix_r1=0
#Si marque de préference et budget entre min et max

if marque_choice=='oui' or marque_choice=='Oui':
  for i in marque_base:
    if i == marque_choisie :
      for ele in base["Produits sans avis"] :
        prix=float(ele['Prix'][0])
        if ele['Marque'][0]==marque_choisie and budget_min<prix <=budget_max:
          if Prix_r1<prix :
            Prix_r1 =prix
            Marque_r1=ele['Marque'][0]
            Nom_r1=ele['Nom'][0]
            Groupe_r1=ele['Groupe']
            Genre_r1=ele['Genre']
            Annee_r1=ele['Année']
        else:
          1
else :
  for ele in base["Produits sans avis"] :
    prix=float(ele['Prix'][0])
    if budget_min<prix <=budget_max:
      if Prix_r1<prix :
        Prix_r1 =prix
        Marque_r1=ele['Marque'][0]
        Nom_r1=ele['Nom'][0]
        Groupe_r1=ele['Groupe']
        Genre_r1=ele['Genre']
        Annee_r1=ele['Année']
    else:
      1



############################Seconde recommandation##############################
Prix_r2=0
#Avis selon budget

for ele in base["Produits avec avis"] :
  prix=float(ele['Prix'])
  if budget_max>=prix :
    if Prix_r2<prix :
      Marque_r2=ele['Marque']
      Nom_r2=ele['Nom']
      Prix_r2=prix
      Avis_r2=ele['Avis']["Nombre d'avis"][0]
      Note_r2=ele['Avis']["Notation"][0]
      Titre_r2 = ele['Avis']['détail']['Avis n1']['Titre'][0]
      Notei_r2 = ele['Avis']['détail']['Avis n1']['Notation'][0]
      Desc_r2 =  ele['Avis']['détail']['Avis n1']['Sous_titre'][0]
      Positif_r2 =  ele['Avis']['détail']['Avis n1']['Positif']
      Négatif_r2 =  ele['Avis']['détail']['Avis n1']['Négatif']
      Rapport_r2 =  ele['Avis']['détail']['Avis n1']['Rapport qualité_prix'][0]

  else :
    if Prix_r2>prix :
      Marque_r2=ele['Marque']
      Nom_r2=ele['Nom']
      Prix_r2=prix
      Avis_r2=ele['Avis']["Nombre d'avis"][0]
      Note_r2=ele['Avis']["Notation"][0]
      Titre_r2 = ele['Avis']['détail']['Avis n1']['Titre'][0]
      Notei_r2 = ele['Avis']['détail']['Avis n1']['Notation'][0]
      Desc_r2 =  ele['Avis']['détail']['Avis n1']['Sous_titre'][0]
      Positif_r2 =  ele['Avis']['détail']['Avis n1']['Positif']
      Négatif_r2 =  ele['Avis']['détail']['Avis n1']['Négatif']
      Rapport_r2 =  ele['Avis']['détail']['Avis n1']['Rapport qualité_prix'][0]



#Affichage des données
print(' ')
print(' ')
print(' ')
print(' ')

print(' Voici les produits que nous vous proposons.')
print(' ')
print(' ')
print('*RECOMMANDATION 1*')
print(' ')
print(' ')
print('NOM DU PRODUIT            ',Nom_r1)
print('MARQUE                    ',Marque_r1)
print("PRIX                      ",Prix_r1)
print("GROUPE DE TRANSMISSION    ",Groupe_r1)
print("GENRE                     ",Genre_r1)
print("ANNÉE                     ",Annee_r1)

print(' ')
print(' ')
print(' ')
print(' ')

print('*RECOMMANDATION 2*')
print(' ')
print(' ')
print('NOM DU PRODUIT           ',Nom_r2)
print('MARQUE                   ',Marque_r2)
print("PRIX                     ",Prix_r2)
print("NOMBRE D'AVIS            ",Avis_r2)
print("NOTE GLOBALE             ",Note_r2)
print(' ')
print("AVIS SUR LE PRODUIT")
print(' ')
print("**",Titre_r2.upper(),"**", "      NOTATION      ", Notei_r2)
print("DESCRIPTION GLOBALE      ",Desc_r2)
print("+                        ",Positif_r2)
print("-                        ",Négatif_r2)
print("RAPPORT QUALITÉ PRIX     ",Rapport_r2)





