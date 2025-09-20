from smtplib import *
import datetime as dt
import random
from dateutil.rrule import weekday

my_email="sumd035@gmail.com"
password="rqkofzodgbvveydu"


now=dt.datetime.now()
week_day =now.weekday()
if week_day==5:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

    print(quote)
    with SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()   #Start security, makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="sumd2023@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")

#
