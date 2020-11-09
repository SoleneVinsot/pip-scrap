import requests
import pdb
import re
import numpy as np


url='https://www.avis-sportifs.com/4407-velos-route-sport'
req=requests.get(url)
contenu=req.text
pat1='>\n      \n        <a href="https://www.avis-sportifs.com/(.+?(?=" class="thumbnail))'
liens=re.findall(pat1,contenu)


lien_match_avis=[]


for i in liens :
  url='https://www.avis-sportifs.com/'+i
  req=requests.get(url)
  contenu=req.text
  pat2='alltricks.fr(.+?(?="><img style="height:30px;))'
  lien_match=re.findall(pat2,contenu)
  if len(lien_match)>1:
    lien_match_avis.append(lien_match[1])

  else :
    continue
np.save("liens_Avis_All",lien_match_avis)




pdb.set_trace()