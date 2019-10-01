import pdb
import json
import folium

## Creation de notre base GeoJSON
Base_geo={}
Base_geo['features']=[]

# Couche 1
feature1={}
feature1['type']='Feature'
feature1['geometry']={ "type": "Polygon", 
    "coordinates": [
        [[2,2], [2,1], [1,1],[1,2],[2,2]]
    ]
}
Base_geo['features'].append(feature1)


# Couche 2
feature2={}
feature2['type']='Feature'
feature2['geometry']={ "type": "Polygon", 
    "coordinates": [
        [[2,0], [2,-1], [1,-1],[1,0],[2,0]]
    ]
}
Base_geo['features'].append(feature2)

## Création de la carte avec les différentes couches
macarte = folium.Map(location=[0,0], zoom_start=5)
macarte.choropleth(Base_geo)
macarte.save('Carte/carte_avec_couches.html')


