import datetime

td=datetime.datetime(2025, 3, 5, 0, 0)
d=datetime.datetime(2025, 3, 8, 0, 0)

a=d-td
print (a.total_seconds())