import requests
from datetime import datetime
from smtplib import *
import time

MY_LAT= 22.962267
MY_LONG= 76.050797

my_email="sumd035@gmail.com"
password="rqkofzodgbvveydu"


def iss_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <=MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return None


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid":'Asia/Kolkata'
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <=sunrise:
        return True
    return None

while True:
    time.sleep(60)
    if iss_iss_overhead() and is_night():
        with SMTP('smtp.gmail.com',port=587) as connection:
            connection.starttls()   #Start security, makes connection secure
            connection.login(user=my_email, password=password)
            send_address="sumd2023@gmail.com"
            connection.sendmail(from_addr=my_email,
                                to_addrs=send_address,
                                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky")




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



