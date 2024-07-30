"""
Les modules date, time et datetime en Python sont très utiles pour travailler avec les dates et les heures.
Voici une description de chacun :

1. Module datetime

Le module datetime est probablement le plus complet des trois et permet de travailler avec
des dates et des heures de manière très flexible.

Principales classes du module datetime :

datetime.date : représente une date (année, mois, jour).
datetime.time : représente une heure (heure, minute, seconde, microseconde).
datetime.datetime : représente une combinaison de date et d'heure.
datetime.timedelta : représente une durée, la différence entre deux dates ou deux heures.

"""

import datetime

# Créer une date
d = datetime.date(2024, 7, 30)
print(d)  # 2024-07-30

# Créer une heure
t = datetime.time(14, 30, 45)
print(t)  # 14:30:45

# Créer une date et une heure
dt = datetime.datetime(2024, 7, 30, 14, 30, 45)
print(dt)  # 2024-07-30 14:30:45

# Ajouter une durée à une date
td = datetime.timedelta(days=10)
new_date = d + td
print(new_date)  # 2024-08-09

"""
2. Module time

Le module time permet de travailler avec le temps (secondes, minutes, heures) et est plus bas niveau que 
datetime. Il est souvent utilisé pour mesurer des intervalles de temps.

Fonctions courantes du module time :

time.time() : retourne l'heure actuelle en secondes depuis l'époque (epoch, le 1er janvier 1970).

time.sleep(seconds) : suspend l'exécution du script pour le nombre de secondes spécifié.

time.ctime() : convertit un temps exprimé en secondes depuis l'époque en une chaîne de caractères.

"""
import time
from datetime import date, datetime

# Heure actuelle en secondes depuis l'époque

current_time = time.time()

print(current_time)  # Par exemple, 1658576745.123456

# Dormir pendant 2 secondes

time.sleep(2)

# Convertir en une chaîne de caractères

print(time.ctime(current_time))  # Par exemple, Mon Jul 25 14:30:45 2024

"""
3. Module calendar

Le module calendar permet de travailler avec des calendriers. 
Il permet de générer des calendriers en format texte ou HTML et de vérifier si 
une année est bissextile, entre autres fonctionnalités.

Fonctions courantes du module calendar :

calendar.month(year, month) : retourne un calendrier pour un mois donné.

calendar.isleap(year) : retourne True si l'année est bissextile.

"""
import calendar

# Imprimer le calendrier de juillet 2024

print(calendar.month(2024, 7))

# Vérifier si 2024 est une année bissextile

print(calendar.isleap(2024))  # True

