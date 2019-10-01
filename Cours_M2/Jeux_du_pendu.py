import random

import pdb
#pdb.set_trace()

liste_mots = ("salut","bande","de","cons")
mot_a_deviner = random.choice(liste_mots)
mot = list (mot_a_deviner)
mot_devine = []
mot_restant = []

mot_affiche = list(mot_a_deviner)
"""mot_affiche=[]

m=0
for i in mot :
  mot_affiche.extend("_")"""





print('Le mot à deviner contient ',len(mot_a_deviner),' lettres. Vous avez 10 chances.')
nombre_restant = len(mot_a_deviner)
mot_fin=mot_a_deviner

nombre_chance = 10

while nombre_chance > 0 :
  lettre = input("Donne moi une lettre  ")
  if lettre == str(lettre) :


    if lettre in mot_a_deviner :
      print("bravo, vous avez deviné le mot contient bien la lettre : ", lettre)
      #lettres_devinees = lettres_devinees.join(lettre)
      #print ("Vous avez devinez les lettres : ", lettres_devinees)
      for i in mot :
        if i == lettre :
          mot_devine.append(i)
          mot_affiche = ["_" if x!=i else x for x in mot_affiche]
          print(mot_affiche)



        else :
          mot_devine.append("_")

          mot_restant.append(i)

        print(mot_affiche)


      print ("Vous avez devinez les lettres : ", '  '.join(mot_affiche))

      mot_a_deviner=''.join(mot_restant)
      mot= mot_a_deviner
      mot_devine = []
      mot_restant = []




      nombre_restant = len(mot_a_deviner)
      print ("Il vous reste ", nombre_restant , "lettre à deviner" )


      if nombre_restant == 0 :
        print("Bravo, vous avez trouvé le mot : ", mot_fin)
        break
      else :
        continue



    else :
      print("cette lettre n'appartient pas au mot à deviner")
      nombre_chance = nombre_chance - 1
      print ("Il vous reste : ", nombre_chance , "chance")
      if nombre_chance == 0 :
        print("vous avez perdu, le mot était : ", mot_a_deviner)
        break
      continue

  else :
    print ("Ceci n'est pas une lettre")
    continue




