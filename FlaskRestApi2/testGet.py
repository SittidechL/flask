#Client Side

import requests
import json
URL="http://127.0.0.1:5000/weather/1"
response=requests.get(URL)
message=response.json()
print(message)
