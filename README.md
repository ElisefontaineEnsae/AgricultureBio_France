# AgricultureBio_France
Projet de Data Science pour le cours de 2ème année de l'ENSAE intitulé "Python for Data Science".

## Projet porté par Fadi Belmahi, Imane Bayoub et Elise Fontaine

### 1) Contexte 

Sans réelle base de données présente pour notre premier choix de sujet nous nous portons sur un autre sujet. **L'agriculture biologique en France : nous raconte-t-on des salades ? **

Données présentes sur data.gouv.fr:

-Parcelles biologiques : https://www.data.gouv.fr/fr/datasets/parcelles-en-agriculture-biologique-ab-declarees-a-la-pac/#/resources

-Achat produits phytosanitaires : https://www.data.gouv.fr/fr/datasets/achats-de-pesticides-par-code-postal/

-Pesticides présent dans les eaux souterraines : https://www.data.gouv.fr/fr/datasets/pesticides-dans-les-eaux-souterraines/

-Professionnels engagés dans le BIO : https://www.data.gouv.fr/fr/datasets/professionnels-engages-en-bio/

-Un webscrapping des données sur les réseaux sociaux pour mesurer une éventuelle évolution de la proportion des commentaires sur le BIO et le sentiment qui en découle.



### 2) Méthodologie 


In fine, avec toutes ses bases de données l'idée est de s'intéresser sur l'Agriculture BIO en France et de voir de potentielle corrélations entre les zones "biologiques" et la consommation effective de pesticide (régression linéaire ?) 

Mettre en lumière une éventuelle externalité négative de l'Agriculture BIO et de la polution des eaux : mapping géospatial. 

Avec les sentiments des consommateurs, mettre en lumière une éventuelle prédiction (via ML) de l'augmentation de l'Agriculture BIO en France le tout accompagné de la base de données des professionnels certifiés BIO.

### 3) Gestion des fichiers volumineux sur le SSP Cloud

Pour éviter d'alourdir le dépôt Git avec des fichiers volumineux, les données ont été stockées sur un bucket S3 accessible via le SSP Cloud. Voici les étapes réalisées pour cette gestion.

---

#### **1. Création d'un bucket et transfert des données**

- Un bucket nommé **`elisefontaine`** a été créé sur le SSP Cloud.
- Un dossier **`diffusion`** a été ajouté dans ce bucket pour contenir les fichiers volumineux.
- Les fichiers locaux ont été transférés dans ce dossier S3 à l'aide d'un script Python nommé **`import_s3fs.py`**, situé dans le dossier `scripts_bucket` de ce dépôt.

##### Script utilisé :
Le script [import_s3fs.py](scripts_bucket/import_s3fs.py) effectue les opérations suivantes :
1. Configure l'accès au bucket S3 avec les clés d'accès (Access Key et Secret Key).
2. Crée le dossier **`diffusion`** dans le bucket S3 s'il n'existe pas.
3. Transfère les fichiers volumineux (comme **GeoPackages**) depuis un chemin local vers le dossier S3.

---

#### **2. Lecture et manipulation des fichiers depuis S3**

Pour éviter de télécharger les fichiers volumineux localement à chaque exécution, les données sont directement lues depuis S3 en mode **lecture** grâce au package Python `s3fs`.

##### Script associé :
Le script **`work_with_s3_data.py`** (à inclure si nécessaire) permet :
1. De lire les fichiers directement depuis S3.
2. De manipuler les données (par exemple, chargement avec `pandas` ou `geopandas`) en utilisant un mode lecture seul.
3. D’enregistrer les résultats dans un autre dossier S3 si nécessaire.

---

#### **3. Comment exécuter les scripts**

##### 3.1. Transférer des fichiers locaux vers S3
Pour transférer des fichiers volumineux dans le bucket S3 :
```bash
python scripts_bucket/import_s3fs.py
