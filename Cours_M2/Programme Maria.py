import folium
import json
import pdb

with open('DPEstado_do_RioFinal.json', 'r') as output:
    Basegeo=json.load(output)

polygon=0
pstrou=0
ptrou=0
multipolygon=0
mstrou=0
mtrou=0
trou=0

for ele in Basegeo['features']: #ele est un dictionnaire, prend tous les élements de cet objet
    if ele['geometry']['type']=='Polygon':
        polygon=polygon+1
        for a in ele['geometry']['coordinates']:
            if a == 1 :
                pstrou=pstrou+1
            else :
                ptrou=ptrou+1
        else:
            multipolygon=multipolygon+1
        if len(ele['geometry']['coordinates'])==1:
            mstrou=pstrou+1
        else :
            mtrou=ptrou+1

print("Le nombre de polygone est de ", polygon, "dont ", ptrou, " avec trou")
print("Le nombre de multipolygone est de ", multipolygon, "dont", mtrou, " avec trou" )
#Un polygone est une liste qui contient une liste détenant toutes les coordonnées de chaque point
#Un polygone sans trou est une liste contenant une liste qui détient tous les coordonnées du polygone puis une liste de coordonnées pour chq trou
#Un multi-polygone = une liste qui contient x nombre de liste de x polygone (cf la structure de chq polygone)
