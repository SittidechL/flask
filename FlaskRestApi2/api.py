#Server Side
from flask import Flask 
from flask_restful import Api,Resource,abort,reqparse,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)


api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"
db=SQLAlchemy(app)

class CityModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    temp=db.Column(db.Integer,nullable=False)
    weather=db.Column(db.String(100),nullable=False)
    people=db.Column(db.String(100),nullable=False)
    
    def __repr__(self):
        return f"City(name={name},temp={temp},weather={weather},people={people})"
 
db.create_all()

#Request Parse
city_add_args=reqparse.RequestParser()
city_add_args.add_argument('name',required=True,type=str,help="Please input name")
city_add_args.add_argument('temp',required=True,type=str,help="Please input temp")
city_add_args.add_argument('weather',required=True,type=str,help="Please input weather")
city_add_args.add_argument('people',required=True,type=str,help="Please input people")

#update
city_update_args=reqparse.RequestParser()
city_add_args.add_argument('name',type=str,help="Please change name")
city_add_args.add_argument('temp',type=str,help="Please change temp")
city_add_args.add_argument('weather',type=str,help="Please change weather")
city_add_args.add_argument('people',type=str,help="Please change people")

resource_field={
    "id":fields.Integer,
    "name":fields.String,  
    "temp":fields.String,
    "weather":fields.String,
    "people":fields.String,            
}


#validate requescls

def notFoundCity(city_id):
    if city_id not in mycity:
        abort(404,message="not found city")

class WeatherCity(Resource):
    def get(self,city_id):   #Read
        result=CityModel.query.filter_by(id=city_id).first()
        if result:
            abort(409,message="Used before")
        return result

    @marshal_with(resource_field)    
    def post(self, city_id):  #Creat
        args = city_add_args.parse_args()
        result=CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404,message="have it")        
        city=CityModel(id=city_id,name=args["name"],temp=args["temp"],weather=args["weather"],people=args["people"])
        db.session.add(city)
        return city,201

    @marshal_with(resource_field)
    def patch(self,city_id):
        args=city_update_args.parse_args()
        result=CityModel.query.filter_by(id=city_id).first()
        if not result:
            abort(404,message="not found city")
        if args["name"]:
            result.name=args["name"]
        if args["temp"]:
            result.name=args["temp"]
        if args["weather"]:
            result.name=args["weather"]
        if args["people"]:
            result.name=args["people"]
        
        db.session.commit()
        return result

#Call
api.add_resource(WeatherCity,"/weather/<int:city_id>")

if __name__ == '__main__':
    app.run(debug=True)
    
#https://www.youtube.com/watch?v=emgRpDDgJ_8    