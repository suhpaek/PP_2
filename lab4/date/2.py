import datetime

td=datetime.datetime.now()
ys=datetime.datetime.now()-datetime.timedelta(days=1)
tm=datetime.datetime.now()+datetime.timedelta(days=1)
print(ys)
print(td)
print(tm)