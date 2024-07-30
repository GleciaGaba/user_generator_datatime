import dateparser

"""
Le module dateparser en Python est une bibliothèque puissante et flexible pour analyser les 
dates à partir de chaînes de caractères dans des formats variés. Il est particulièrement utile 
lorsque les dates sont dans des formats non standard ou dans différentes langues.
"""

today = dateparser.parse("aujourd'hui")
print(today)

tomorrow = dateparser.parse("demain")
print(tomorrow)

in_a_month = dateparser.parse("dans un mois")
print(in_a_month)

last_month = dateparser.parse("Il y a un mois")
print(last_month)

midnight = dateparser.parse("One year ago at midnight")
print(midnight)

"""
Principales fonctionnalités de dateparser :

Analyse des dates dans divers formats :

dateparser peut interpréter des dates écrites sous différentes formes et dans 
différentes langues sans besoin de spécifier explicitement le format.
Prise en charge de multiples langues :

Il supporte de nombreuses langues, ce qui permet d'analyser des dates écrites 
dans ces langues sans effort supplémentaire.
Traitement des dates relatives :

Il peut comprendre des dates relatives comme "il y a 3 jours", "la semaine prochaine", etc.
Configuration flexible :

Vous pouvez configurer dateparser pour s'adapter à des besoins spécifiques, 
comme la définition de la première journée de la semaine, l'utilisation d'un fuseau horaire spécifique, etc.


"""