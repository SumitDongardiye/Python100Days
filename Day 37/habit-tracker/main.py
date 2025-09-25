import requests
from datetime import *
from aiohttp.helpers import TOKEN

USERNAME="sumitdongardiye"
TOKEN= "jk34klasf834kj42k"
GRAPH_ID= "graph1"
pixela_endpoint= "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "Hours",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today= date.today()

posting_pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many subjects did you studied today? "),
}

# response=requests.post(posting_pixel_endpoint,json=pixel_config, headers=headers)
# print(response.text)

date_to_replace="20250925"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_replace}"
new_pixel_data = {
    "quantity": "0",
}

# response=requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_replace}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)