from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("Name is ")
    phonenumber = StringField("Phone Number is ")
    submit = SubmitField("Submit")

@app.route("/", methods=['GET','POST'])
def index():
    name = False
    phonenumber = False
    form=MyForm()
    if form.validate_on_submit():
        name = form.name.data
        phonenumber = form.phonenumber.data
        form.name.data=""
        form.phonenumber.data=""
    return render_template("index.htm", form=form,name=name,phonenumber=phonenumber)

@app.route("/",methods=['POST'])
def phonebook():
    name = request.form("Name")
    phonenumber=request.form("Phonenumber")
    connection = sqlite3.connect(currentdirectory + "\phonebook.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO phonebook VALUES('(n)',{pnm})".format(n=name,pnm=phonenumber)
    cursor.execute(query1)
    connection.commit()

if __name__ == "__main__":
    app.run(debug=True)


#https://www.youtube.com/watch?v=U1JUicQzGMI
#https://getbootstrap.com/docs/5.1/components/accordion/