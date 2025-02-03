import calendar
from datetime import time
from datetime import date
from datetime import datetime
dat=date.today()
year_cur=dat.year
month_cur=dat.month
print (calendar.month(year_cur,month_cur))
# print(dat)