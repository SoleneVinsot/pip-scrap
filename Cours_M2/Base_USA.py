
#Exercice définitions
""""
def multi(a) :
    b=0
    while b<11 :
        c=a*b
        b+=1
        print(c)
        


print(multi(5))

import requests

def code(url,nom) :
    request = requests.get(url)
    body=request.text
    with open (nom,'w',encoding='utf8') as file :
        file.write(body)
    
    



code('https://www.kingsfleet.fr/?fbclid=IwAR1KWpKSCokcjUss-RV7_80bBBLI5geXFw3V4GtaOYrXRzw15d1nD4teoo0','toto.txt')
"""


import csv
with open('US_Unemployment_Oct2012.csv','r') as output:
    chomage=csv.reader(output,delimiter=',')
    for row in chomage :
        
        







