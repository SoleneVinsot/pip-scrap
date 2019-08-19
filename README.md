# PIP-SCRAP

## Installation

- Installer chromedriver : https://chromedriver.chromium.org/ puis déplacer le fichier dézipper à la racine du projet.

- `pip install -r requirements.txt` ou `pip3 install -r requirements.txt`

## Définition des scrappers

### Scrapper 1

Récupère tous les liens du site [https://www.opinionsystem.fr](https://www.opinionsystem.fr) (*Opinion System est le N°1 des avis clients contrôlés pour les professionnels du service et de l'immobilier*) et extrait les informations suivantes :

* adresse ;
* ville ;
* pays ;
* numéro de téléphone ;
* entreprise ;
* email ;

Démarrer le script `getLinks.py` pour récupérer les liens.
Ensuite, démarrer le script `scrapper.py` pour extraire les informations.

### Scrapper 2

Extrait les informations du site [https://www.magazine-decideurs.com](https://www.magazine-decideurs.com/classements/propriete-industrielle-brevets-contentieux-classement-2019-cabinet-d-avocats-france?locale=fr) (*Classement des cabinets d'avocats*) :

* numéro de téléphone ;
* cabinet ;
* nom ;
* métiers ;
* emails des avocats ;
* emails des cabinets ;

Démarrer le script `scrapper.py` pour extraire les informations.

### Scrapper 3

Extrait les informations du site [http://www.avocatparis.org/](http://www.avocatsparis.org/Eannuaire/CMSRecherche2.aspx?wmode=transparent) (*Liste des cabinets d'avocats*) :

* numéro de téléphone ;
* nom ;
* emails ;
* fax ;
* adresses ;
* activités ;

Démarrer le script `scrapper.py` pour extraire les informations.

### Scrapper 4

Extrait les informations du site [https://www.barreau-marseille.avocat.fr/](https://www.barreau-marseille.avocat.fr/fr/annuaire/page-1?&full=&nom=&specialites=&recherche_annuaire-submit=Ok) (*Liste des cabinets d'avocats*) :

* Nom ;
* Email ;
* Adresse ;
* Numéro ;
* Fax ;
* Activité ;

Démarrer le script `scrapper.py` pour extraire les informations.

