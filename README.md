# L'agriculture biologique: nous raconte-t-on des salades ?
*Ce projet est réalisé dans le cadre du cours de Python pour la Data Science donné par Lino Galiana à l'ENSAE Paris en 2024.*

Auteurs: *Fadi Belmahi, Imane Bayoub et Elise Fontaine*

## Sujet:  
Les eaux souterraines constituent une ressource essentielle pour l’approvisionnement en eau potable, l'irrigation des terres agricoles et la préservation des écosystèmes. Cependant, elles sont particulièrement vulnérables aux pollutions diffuses issues des pratiques agricoles, notamment les nitrates et les résidus de pesticides. Face à ce défi environnemental, l’agriculture biologique est régulièrement mise en avant comme une solution durable. Comme le souligne l’Agence Bio, « la présence de parcelles en agriculture biologique constitue donc l’un des leviers les plus efficaces pour reconquérir et préserver la qualité de l’eau. »

Malgré cet espoir, la réalité des sols et des eaux souterraines en France est complexe. Si l’agriculture biologique progresse, elle coexiste avec des pratiques agricoles conventionnelles souvent intensifiées. Ce contexte soulève une question cruciale : les bénéfices attendus de l’agriculture biologique sont-ils suffisamment puissants pour contrebalancer les pressions exercées par les autres systèmes de production agricole ?

Ce projet de data science vise à analyser l’impact réel de l’agriculture biologique sur la pollution des eaux souterraines en France. En utilisant des données historiques couvrant la période de 2007 à 2013, marquée par l'émergence significative de l'agriculture biologique, nous chercherons à comprendre si cette transition agricole a contribué à une amélioration mesurable de la qualité des eaux ou si d'autres facteurs, comme l’intensification des pratiques conventionnelles, en ont annulé les effets.

## Problématique
L’agriculture biologique peut-elle réellement compenser les impacts négatifs des pratiques agricoles conventionnelles sur les eaux souterraines, ou son effet est-il dilué par une intensification accrue sur les parcelles non biologiques ?

## Données utilisés

Données présentes sur data.gouv.fr:

-Parcelles biologiques : https://www.data.gouv.fr/fr/datasets/parcelles-en-agriculture-biologique-ab-declarees-a-la-pac/#/resources

-Achat produits phytosanitaires : https://www.data.gouv.fr/fr/datasets/achats-de-pesticides-par-code-postal/

-Pesticides présent dans les eaux souterraines : https://www.data.gouv.fr/fr/datasets/pesticides-dans-les-eaux-souterraines/

-Professionnels engagés dans le BIO : https://www.data.gouv.fr/fr/datasets/professionnels-engages-en-bio/

-Un webscrapping des données sur les réseaux sociaux pour mesurer une éventuelle évolution de la proportion des commentaires sur le BIO et le sentiment qui en découle.

In fine, avec toutes ses bases de données l'idée est de s'intéresser sur l'Agriculture BIO en France et de voir de potentielle corrélations entre les zones "biologiques" et la consommation effective de pesticide (régression linéaire ?) 

Mettre en lumière une éventuelle externalité négative de l'Agriculture BIO et de la polution des eaux : mapping géospatial. 

Avec les sentiments des consommateurs, mettre en lumière une éventuelle prédiction (via ML) de l'augmentation de l'Agriculture BIO en France le tout accompagné de la base de données des professionnels certifiés BIO.

## Modèle utilisé
