from datetime import datetime

ippudu = datetime.now()
sec = ippudu.timestamp()
print(ippudu)

now = datetime.now()
t = now.strftime("%S:%M:%H")
print(t)
l = now.strftime("%A")
print("The day is:", l)

date_string = "3 February, 2003"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

from datetime import date
d = date(2021, 5, 3)
print(d)
print(d.today())

from datetime import date, datetime
today = date.today()
abhinav_bday = date(2003, 3, 2)

abhinav_age = today - abhinav_bday
print("My age is: ", abhinav_age)