from multiprocessing.connection import Client
import os
from twilio.rest import Client

import requests

account_sid = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("OWM_AUTH_TOKEN")



OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="e76d8b244cec50795e9674212a1f7837"
lat=23.831457
lon=91.286781
weather_params={
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt":4,
}

response= requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
will_rain = True

for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    print("Rain in 5 min")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring umbrella",
        from_="+12313542991",
        to="+917415258876",
    )