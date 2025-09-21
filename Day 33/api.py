# An API is set of commands, functions, protocols,
# and objects that programmers can use to create
# software or interact with an external system.
import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  #Used to generate exceptino, if there is some bad request


data=response.json()

longitude=data['iss_position']['longitude']
latitude=data['iss_position']['latitude']

iss_position= (longitude,latitude)
print(iss_position)