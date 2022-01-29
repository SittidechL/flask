from flask import Flask, render_template, request
import sqlite3 as sql

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")


app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/enternew')
def new_student():
   return render_template('student.htm')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect(db_path) as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.htm",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect(db_path)
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
    
#https://pythonbasics.org/flask-sqlite/