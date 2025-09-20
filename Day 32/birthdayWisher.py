##################### Normal Starting Project ######################
from smtplib import *
import datetime as dt
import pandas as pd
import random
from pandas.core.interchange.dataframe_protocol import DataFrame

my_email="sumd035@gmail.com"
password="rqkofzodgbvveydu"

now=dt.datetime.now()
day=now.day
month=now.month
today=(month, day)

data=pd.read_csv("birthdays.csv")
birthday_dict= {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person=birthday_dict[today]
    file_path= f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        final_content=content.replace("[NAME]",birthday_person["name"])

    with SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()   #Start security, makes connection secure
        connection.login(user=my_email, password=password)
        send_address=birthday_person["email"]
        connection.sendmail(from_addr=my_email,
                            to_addrs=send_address,
                            msg=f"Subject:Happy Birthday!\n\n{final_content}")
