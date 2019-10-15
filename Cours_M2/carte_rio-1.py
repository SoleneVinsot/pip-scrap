# -*- coding: utf8 -*-
import csv
import pdb
import json
import folium

Center=['43', '20', '25', '9', '37', '10', '36', '19', '41', '28', '27', '17', '16 e 42', '32', '35', '7', '14', '6', '18', '33', '21', '24', '29', '39', '38', '23', '34', '31', '30', '15 e 11', '40', '22 e 45', '44', '26','5','13','12','4','1']
Periphery=['54', '81', '72', '51', '78', '52', '75', '66', '62', '82', '63', '60', '48', '50', '53', '58', '56', '65 e 67', '57', '76', '59', '77', '64', '61', '74', '79', '55', '73']
Country_side=['93', '146', '92', '154', '158', '96', '110', '138', '98', '167', '99', '89', '153', '122', '101', '119', '120', '140', '165', '137', '151', '126 e 132', '124', '107', '143 e 148', '147', '159', '156', '135', '129', '134', '123 e 130', '118', '168', '145', '91', '128', '144', '155', '105', '106', '97', '88', '166', '121', '90', '95', '125', '136', '127', '100', '111', '141', '71 e 70', '157', '142', '94', '108', '139', '109', '152', '104', '112']


def my_color_function(feature):
	dp = str(feature['properties']['DP'])
	if dp in Center:
		return 'yellow'

	elif dp in Periphery:
		return 'green'

	elif dp in Country_side:
		return 'blue'


def my_color_opacity(feature):
	dp = str(feature['properties']['DP'])
	if dp in Center:
		return 1

	elif dp in Periphery:
		return 0.6

	elif dp in Country_side:
		return 0.2

with open('Data/DPEstado_do_RioFinal.json') as gd:
	geo_data_DP = json.load(gd)



macarte = folium.Map(location=[-22.94,-43.42], zoom_start=9)
folium.GeoJson(geo_data_DP,style_function=lambda feature: {'color': 'black','fillColor': my_color_function(feature), 'weight' : 0.6, 'fillOpacity' : my_color_opacity(feature)}).add_to(macarte)
macarte.save('CarteDPEstado.html')






