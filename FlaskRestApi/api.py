#Server Side
from flask import Flask 
from flask_restful import Api,Resource,abort
app = Flask(__name__)
api=Api(app)

mycity={
    1:{"1":"ชลบุรี","Weather":"อากาศร้อนอบอ้าว","people":1500},
    2:{2:"ระยอง","Weather":"ผนตก","people":2000},
    3:{3:"กรุงเทพ","Weather":"หนาว","people":2500},   
}

#validate request
def notFoundCity(city_id):
    if city_id not in mycity:
        abort(404,message="not found city")

class WeatherCity(Resource):
    def get(self,city_id):
        notFoundCity(city_id)
        return mycity[city_id]
        #return {"data":"Select Resource = " +city_id }
    def post(self, city_id):
        notFoundCity(city_id)
        return mycity[city_id]
        #return {"data":"Create Resource = " +city_id}

#Call
api.add_resource(WeatherCity,"/weather/<int:city_id>")

if __name__ == '__main__':
    app.run(debug=True)