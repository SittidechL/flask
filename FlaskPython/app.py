from flask import Flask,render_template
from flask_restful import Api,Resource,abort,reqparse,marshal_with,fields
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

app = Flask(__name__)




@app.route("/")
def hello():
    age="Python Flask"
    return render_template('index.htm',data=age)
    


if __name__ == "__main__":
    app.run(debug=True)
    
