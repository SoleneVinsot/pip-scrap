import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import requests
import html
import csv
import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

# Nom du fichier de sauvegarde
saveAs = ''

# URL à scrapper
urlToScrap = 'http://www.avocatsparis.org/Eannuaire/CMSRecherche2.aspx?wmode=transparent'

# Chromedriver doit être installé et placé à la racine du projet
driver = webdriver.Chrome(executable_path = os.path.join(os.getcwd(), 'chromedriver'), chrome_options = chrome_options)
driver.implicitly_wait(3)
driver.get(urlToScrap)

activities = ["Droit de la circulation et des transports","Dommages corporels et matériels","Droit de la consommation","Contentieux, médiation, arbitrage","Droit de la faillite et du surendettement","Droit de la famille","Droit de la sécurité sociale","Droit de l'environnement","Droit de l'immigration et d'asile","Droit de l'UE","Droit des affaires","Droit des biens","Droit des successions","Droit des technologies de l'information","Droit du travail","Droit fiscal","Droit pénal","Droit public","Droits de l'homme et libertés publiques","Propriété intellectuelle"]


for activity in activities : 

    # Choisir l'arrondissement
    elem = driver.find_element_by_id("_ctl0_Corps_txtRSArrondissement")
    elem.send_keys("75008")

    option = driver.find_element_by_id('_ctl0_Corps_ddlRSActivite')
    option.send_keys(activity) 
    links = []
    time.sleep(1)

    # Selectionne parmi les choix proposes
    driver.find_element_by_id("_ctl0_Corps_imgbtnRecherche").click()


    currentPage = 1
    while currentPage < 100 :
        
        j = 2
        while j < 12 :
            id = driver.find_element_by_xpath('//*[@id="_ctl0_Corps_dgListeResultat"]/tbody/tr['+str(j)+']/td/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[1]/td[1]/a')

            link = id.get_attribute('href')
            print(link)
            j += 1
            links.append(link)

        nextPage = driver.find_element_by_id("_ctl0_Corps_DataGridPager1_Page_" + str(currentPage + 1))
        # print(nextPage.getText())
        # if not nextPage :
        #     break
        # else :
        #     nextPage.click()
        #     currentPage += 1




driver.quit()
    

#<a href="CMSResultat2.aspx?cnbf=d13171b9966b286e845ce8d08c2130f6&amp;p=plan&amp;adp=23 RUE HENRI BARBUSSE%2B75005%2BPARIS"><strong>Florent GALLAIRE</strong></a>



requests_headers={'User-Agent':"(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"}

liste_noms=[]
liste_adresses=[]
liste_numeros=[]
liste_fax=[]
liste_mails=[]
liste_activites=[]
liste_cabinets=[]
liste_act=[]
cabinets=[]

for i in links :
    req=requests.get(i, headers=requests_headers, timeout=10)
    contenu=req.text
    contenu=html.unescape(contenu)

    #noms des avocats
    pat1='<span id="_ctl0_Corps_lblNom" tabindex="2">(.+?(?=</span>))'
    nom=re.findall(pat1,contenu)
    liste_noms.extend(nom)

    #adresse à Paris
    pat2='<span id="_ctl0_Corps_lblAdresse" tabindex="2">(.+?(?=</span>))'
    adresse=re.findall(pat2,contenu)
    liste_adresses.extend(adresse)   

    #numéro de téléphone
    pat3='<span id="_ctl0_Corps_lblTelephone" tabindex="2">(.+?(?=</span>))' 
    numero=re.findall(pat3,contenu)
    liste_numeros.extend(numero)

    #numéro de fax
    pat4='<span id="_ctl0_Corps_lblTelecopie" tabindex="2">(.+?(?=</span>))'
    fax=re.findall(pat4,contenu)
    liste_fax.extend(fax)

    #mail
    pat5='<a href="mailto:(.+?(?=">))'
    if 'href="mailto:' in contenu :
        mail=re.findall(pat5,contenu)
        liste_mails.extend(mail)
    else :
        liste_mails.append('NA')

    #Activités dominantes
    pat6='<span id="_ctl0_Corps_lblActivitesDominantes" tabindex="2">(.+?(?=</span>))'
    act=re.findall(pat6,contenu)
    liste_act.extend(act)


    #Lien cabinet
    pat7='<a href="CMSResultat(.+?(?=">))'
    if 'href="CMSResultat' in contenu:
        cabinet=re.findall(pat7,contenu)
        liste_cabinets.append(cabinet)
    else :
        liste_cabinets.append('inconnu')
    



for e in liste_act:
    e=e.replace('<br />',' ; ')
    liste_activites.append(e)

for l in liste_cabinets :
    for a in l:
        a=a.replace('2','')
    url='http://www.avocatsparis.org/Eannuaire/CMSFicheGroupe'+str(a)
    req=requests.get(url, headers=requests_headers, timeout=10)
    contenu2=req.text
    contenu2=html.unescape(contenu2) 
    if '<strong>Structure non exerçante</strong>' in contenu :
        cabinets.extend('erreur')
    else : 

        if l is 'inconnu' : 
            cabinets.append(l)
        else:
            pat8='<span id="_ctl0_Corps_lblDesignation" tabindex="2">(.+?(?=</span>))'
            cabinets.extend(re.findall(pat8,contenu2))

#<span id="_ctl0_Corps_lblDesignation" tabindex="2">JONES DAY</span>
#<span id="_ctl0_Corps_lblDesignation" tabindex="2">ASIALLIANS</span>

print(len(liste_noms))
print(len(liste_adresses))
print(len(liste_numeros))
print(len(liste_fax))
print(len(liste_mails))
print(len(liste_activites))
print(len(liste_cabinets))
print(len(cabinets))

K=[liste_noms,liste_mails,liste_adresses,liste_numeros,liste_fax,liste_activites]

with open("TOTOR.csv", "w",encoding='utf-8') as outfile:
        data=csv.writer(outfile,delimiter=';',lineterminator='\n')
        data.writerow(['Nom','Email','Adresse','Numéro','Fax','Activités'])
        for row in zip(*K):
            data.writerow(row)





#lou=driver.find_element_by_class("corps3newannuaire&quot;")



#<script type="text/javascript" src="http://www.avocatsparis.org/script/wreport.js"></script>

#<td class="corps3newannuaire&quot;" width="740px"><div class="principal" align="left"><div class="principal2"><div class="haut"><div class="coingh"></div><div class="coindh"></div></div><div class="data"><table border="0" width="740px" align="center"><tbody><tr class="lien3"><td width="400px"><a href="CMSResultat2.aspx?cnbf=13611d684c259e6b60f18878ad1c0e25&amp;p=plan&amp;adp=50 RUE DAREAU%2B75014%2BPARIS"><strong>Géraud BOMMENEL</strong></a></td><td width="250px"></td><td></td></tr><tr class="lien3"><td><span class="newannuair10px">Inscrit&nbsp;<a href="https://ssl.avocatparis.org/LoginTB.aspx?secure=13611d684c259e6b60f18878ad1c0e25"><img height="21" src="../img/habillage/ikey_transparent.gif" width="80" align="absMiddle" border="0"></a></span></td><td class="coprs2"><strong>Tél.: </strong><span class="newannuair10px">0142221095</span></td><td><a href="CMSResultat2.aspx?cnbf=13611d684c259e6b60f18878ad1c0e25&amp;p=plan&amp;adp=50 RUE DAREAU%2B75014%2BPARIS"><img src="img/plusinfo.png" alt="Afficher plus d'information" border="0"></a></td></tr><tr class="lien3"><td><span class="newannuair10px">50 RUE DAREAU 75014      PARIS</span></td><td><strong>Fax.: </strong><span class="lien3">0142221232</span></td><td></td></tr><tr><td class="newannuaircorps2"><a href="CMSResultat2.aspx?cnbf=13611d684c259e6b60f18878ad1c0e25&amp;p=plan&amp;act=posi&amp;adp=50 RUE DAREAU%2B75014%2BPARIS">plan</a>&nbsp;<a href="CMSResultat2.aspx?cnbf=13611d684c259e6b60f18878ad1c0e25&amp;I=Itinéraire&amp;adi=50 RUE DAREAU%2B75014%2BPARIS">Itinéraire</a></td><td><strong>mail : </strong><span class="lien3"><a href="mailto:gbommenel@selarljuris.org">gbommenel@selarljuris.org</a></span></td><td></td></tr></tbody></table></div><div class="bas"><div class="coingb"></div><div class="coindb"></div></div></div></div></td>

