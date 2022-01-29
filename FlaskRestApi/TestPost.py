#Client Side2
import requests
import jsons
URL="http://127.0.0.1:5000/weather/4"

response=requests.post(URL)
message=response.json()
print(message)
#print(message["data"])
