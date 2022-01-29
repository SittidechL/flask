#Client Side2
import requests
import jsons
URL="http://127.0.0.1:5000/weather/2"
payload={"id":"2","name":"Chonburi","temp":"30","weather":"หนาวมาก","people":"20000"}
response=requests.post(URL,data=payload)
print(response)
#print(message["data"])
