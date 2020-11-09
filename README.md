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

### Scrapper 5

Extrait les informations des sites [https://www.avis-sportifs.com/](https://www.avis-sportifs.com/) (*Recensement d'avis sur les équipements de sport*), [https://www.decathlon.fr/](https://www.decathlon.fr/) (*Équipements de sport*) et [https://www.go-sport.com](https://www.go-sport.com/running/) (*Équipements de sport*) :

* Nom du produit ;
* Catégorie du produit ;
* Marque ;
* Prix ;
* Nombre d'avis ;

Démarrer le script `scrapper_AS.py` pour récupérer les données du site avis-sportifs.
Ensuite, démarrer le script `scrapper_total.py` pour récuperer les données collectées dans le premier site, extraire les informations et analyser les données.

Cette étude à pour but de répondre à la problématique : "Quels sont les déterminants de la popularité d’un popularité d’un produit ?"

L'analyse des données comprend différentes visualisations, analyses statistiques et économétriques.


### Scrapper 6

Extrait des informations des sites [https://www.avis-sportifs.com/](https://www.avis-sportifs.com/) (*Recensement d'avis sur les équipements de sport*), [https://www.alltricks.fr/](https://www.alltricks.fr/) (*Matériel de cyclisme*) puis exerce une analyse statistique des données et permet d'accéder à la recommandation de produits via un questionnaire.


1) « scrapper_liens.py »

	Le premier scrapper, permet de récupérer tous les liens en format numpy du site https://www.alltricks.fr/ à l’aide d’un chrome driver. Ainsi, la liste des liens de chaque page produit des vélo de route du site est enregistrée au nom de « liens.npy ».


2) « scrapper_produit.py »

	Le second scrapper, permet de collecter les informations sur les produits dont les liens ont été extraits dans le premier scrapper. Ce scrapper a pour but d’enregistrer les informations suivantes dans un fichier Json, « base_alltricks.json ».

* nom du produit ;
* identifiant du produit ;
* marque du produit ;
* prix du produit ;
* genre (masculin, féminin) ;
* groupe de transmission du produit (marque et modèle) ;
* année de sortie du produit.

3) « scrapper_avis_liens.py »

	Ce scrapper, a la même utilité que le premier scrapper. Il récupère les liens des fiches produit de la catégorie concernant les vélos de route du site https://www.avis-sportifs.com/ enregistrés sous le nom de « liens_Avis_All.npy ». Ensuite, le scrapper extrait dans chaque fiche produit les liens vers les pages du site Alltricks dans le cas ou le produit est répertorié dans le site Alltricks.


4) « scrapper_produit_AS.py »

	Il extrait les informations des produits du site https://www.avis-sportifs.com dont les informations sont trouvables sur le site de l’entreprise Alltricks et extrait les informations du site Alltricks pour ces produits. De plus, ce scrapper fusionne les deux bases créées pour enregistrer la totalité des données dans un fichier Json, « base_totale.json ». Les informations extraites pour les produits notés par la communauté Avis_Sportifs sont les suivantes :

* nom du produit ;
* identifiant du produit ;
* marque du produit ;
* prix du produit ;
* Nombre d'avis ;
* Notation totale du produit;
* Avis de l'utilisateur ;
* Rapport qualité prix du produit ;
Notation individuelle du produit.


5) « statistiques.py »

	Ce scrapper permet d’effectuer des statistiques, grâce au module matplotlib, sur les données recueillies dans les différents scrapper précédents afin de connaître les informations à prendre en considération dans la recommandation de produits. Les données suivantes sont utilisées :

* Marque du produit ;
* Genre (sexe masculin, féminin ou neutre) ;
* Prix du produit ;
* Groupe de transmission du produit.


6) « recommandation.py »

	Ce dernier scrapper traite les données du fichier base_totale.json afin de recommander à l'utilisateur des produits selon des critères demandés en amont. Les critères sont les suivants :

* Recommandation 1 : marque, budget minimal, budget maximal ;
* Recommandation 2 : avis, budget maximal.

