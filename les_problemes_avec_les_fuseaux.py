"""
UTC, ou Temps Universel Coordonné (Coordinated Universal Time en anglais), est la norme de
temps internationale utilisée comme référence principale pour l'heure mondiale.

Voici une définition plus détaillée :

Définition de l'UTC
UTC (Temps Universel Coordonné) est la norme de temps internationale basée sur le temps atomique.
Il est utilisé pour synchroniser l'heure à travers le monde et sert de référence pour les fuseaux horaires globaux.

Caractéristiques de l'UTC
Norme de Temps Universelle :

UTC est le point de référence pour tous les fuseaux horaires du monde. Les fuseaux horaires sont
exprimés en fonction de leur décalage par rapport à UTC (par exemple, UTC+1, UTC-5).
Basé sur le Temps Atomique International (TAI) :

L'UTC est calculé à partir du Temps Atomique International, qui est extrêmement précis grâce aux horloges atomiques.
Ajustements avec les Secondes Intercalaires :

Pour rester synchronisé avec la rotation de la Terre, l'UTC est ajusté occasionnellement avec
des secondes intercalaires. Ces ajustements compensent les variations dans la vitesse de rotation de la Terre.
Pas de Changements Saisonniers :

Contrairement à certains fuseaux horaires locaux, l'UTC ne change pas avec les saisons,
il n'a pas d'heure d'été ou d'heure d'hiver.
Utilisation Globale :

L'UTC est utilisé dans les systèmes de navigation, d'aviation, de communication, et dans de
nombreuses applications informatiques où une synchronisation précise du temps est essentielle.
Pourquoi l'UTC est Important
Synchronisation Internationale :

L'UTC permet aux systèmes de différentes parties du monde de fonctionner de manière synchronisée,
facilitant les communications et les transactions internationales.
Standardisation :

En utilisant une seule norme de temps, il est possible d'éviter les confusions et les erreurs qui
peuvent survenir avec les différents fuseaux horaires locaux.
Applications Techniques :

Les systèmes GPS, les serveurs de temps sur internet, les transactions bancaires internationales,
et de nombreuses autres technologies critiques dépendent de l'UTC pour une synchronisation précise.
Exemple d'Utilisation
Par exemple, si vous devez programmer un événement qui doit être coordonné à travers plusieurs
fuseaux horaires, vous utiliseriez l'UTC pour vous assurer que tout le monde se réfère à la même heure :


EDT, EST

Eastern Daylight Time, Eastern Standard Time


PDT, PST

"""


from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


"""montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))

march_8 = march_7_utc + timedelta(days=1)
march_8 = march_8.astimezone(montreal_tz)

print(march_8)"""


utc = ZoneInfo("UTC")
montreal_tz = ZoneInfo("America/Montreal")

march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_10 = datetime(2020, 3, 10, 13, 0, 0, tzinfo=montreal_tz)

march_7_utc = march_7.astimezone(utc)
march_10_utc = march_10.astimezone(utc)

print(march_10 - march_7)
print(march_10_utc - march_7_utc)


"""
Pourquoi les Résultats Peuvent Être Différents
Le code compare deux différences de temps :

march_10 - march_7 : Cette différence est calculée dans le fuseau horaire de Montréal.
march_10_utc - march_7_utc : Cette différence est calculée dans le fuseau horaire UTC.
Le changement d'heure d'été (Daylight Saving Time, DST) peut affecter le résultat. 
Si, entre le 7 mars et le 10 mars 2020, Montréal passe à l'heure d'été, une heure 
sera "perdue", car les horloges seront avancées d'une heure. Cela se traduira par une 
différence de temps d'une heure entre les deux résultats.

Résultat Attendu
Sans changement d'heure : Les deux différences devraient être identiques.
Avec changement d'heure : La différence en UTC serait plus grande d'une heure par rapport à celle en heure locale de Montréal.

Conclusion
Ce code montre comment travailler avec les fuseaux horaires en Python en utilisant le module zoneinfo. 
Il permet de voir comment les dates et heures peuvent être converties entre différents fuseaux horaires et 
comment les changements de fuseau horaire (comme le passage à l'heure d'été) 
peuvent affecter les calculs de différence de temps.

"""