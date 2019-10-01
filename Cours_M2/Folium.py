import folium
import csv
import pdb
import json

"""#carte de paris
paris = folium.Map(location = [48.856578, 2.351828], zoom_start = 12.2)

lat=48.8581
lon=2.2944

# Tour Eiffel - carré rouge


with open('Cours_python_M2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        #pdb.set_trace()
        if row[0] != "Monument" :
            lat=float(row[1])
            lon=float(row[2])
            folium.Marker([lat,lon],popup=row[0]).add_to(paris)






#folium.RegularPolygonMarker([lat,lon],color='none',fill_color='red',number_of_sides=4,radius=5,popup='Tour Eiffel').add_to(paris)

paris.save('Carte_de_paris.html')
"""

with open('DPEstado_do_RioFinal.json','r') as output:
    Base_geo=json.load(output)
 


