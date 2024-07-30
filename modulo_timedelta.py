from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta

"""
timedelta peut représenter des durées en jours, secondes et microsecondes. 
Il peut également accepter des millisecondes, minutes, heures et semaines 
comme arguments, qui sont convertis en jours, secondes et microsecondes.

"""

"""timedelta(days=20)
datetime.timedelta(days=20)"""

now = datetime.now()
now_in_15_days_minus_5_hours = now + timedelta(days=15, hours=-5)

print(now)

print(now_in_15_days_minus_5_hours)

feb_27_2022 = datetime(2022, 2, 27)

print(feb_27_2022 + timedelta(days=3))


now1 = datetime.now()

now_in_2_months = now1 + relativedelta(months=14)

print(now1)
print(now_in_2_months)

