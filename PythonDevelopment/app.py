from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, RadioField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ")
    isAccept = BooleanField("Accept?")
    #gender = RadioField('Sex',Choices=[('male','Male'),('femal','Femal'),('Other','Other')])
    submit = SubmitField("บันทึก")

@app.route("/", methods=['GET','POST'])
def index():
    name = False
    isAccept = False
    form=MyForm()
    if form.validate_on_submit():
        name = form.name.data
        isAccept = form.isAccept.data
        form.name.data=""
        form.isAccept.data=""
    return render_template("index.htm", form=form,name=name,isAccept=isAccept)

if __name__ == "__main__":
    app.run(debug=True)


#https://www.youtube.com/watch?v=U1JUicQzGMI
#https://getbootstrap.com/docs/5.1/components/accordion/