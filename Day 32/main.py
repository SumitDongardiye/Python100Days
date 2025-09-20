from smtplib import *

my_email="sumd035@gmail.com"
password="rqkofzodgbvveydu"

with SMTP('smtp.gmail.com',port=587) as connection:
    connection.starttls()   #Start security, makes connection secure

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="sumd2023@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
