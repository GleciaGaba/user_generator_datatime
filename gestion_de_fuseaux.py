"""
La DZ Database (ou Dateparser Time Zone Database) est une composante utilisée par
le module dateparser pour gérer les fuseaux horaires. Lorsque vous utilisez
dateparser pour analyser des dates, il peut être nécessaire de spécifier ou de comprendre
le fuseau horaire associé aux dates analysées, et c'est là qu'intervient la DZ Database.

Caractéristiques de la DZ Database :
Informations sur les fuseaux horaires :

La DZ Database contient des informations détaillées sur les fuseaux horaires,
ce qui permet à dateparser de comprendre et de manipuler les dates et heures
en tenant compte des différences de fuseaux horaires.
Mises à jour régulières :

La base de données des fuseaux horaires est régulièrement mise à jour pour
refléter les changements dans les règles de temps partout dans le monde,
comme les changements de l'heure d'été.
Intégration avec dateparser :

Lors de l'analyse de dates, dateparser utilise la DZ Database pour résoudre
correctement les dates et heures en fonction des fuseaux horaires spécifiés
ou implicites dans les chaînes de caractères.
Utilisation de dateparser avec les fuseaux horaires
Voici comment vous pouvez utiliser dateparser pour analyser des dates avec des fuseaux horaires :

Installation
Tout d'abord, assurez-vous d'avoir installé dateparser :

"""

from datetime import datetime
from zoneinfo import ZoneInfo


now = datetime.now()
print(now.tzinfo)


now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))

print(now_in_vancouver)

now_in_montreal = datetime.now(tz=ZoneInfo("America/Montreal"))
print(now_in_montreal)

now_in_natal = datetime.now(tz=ZoneInfo("America/Recife"))
print(now_in_natal)


