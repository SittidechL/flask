from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Hello():
    return render_template("index.htm")

@app.route('/checkbox', methods=['GET', 'POST'])
def checkbox():
    #if request.method == 'POST':
    #    sw = request.form.get['on']
    return render_template("checkbox2.htm")

@app.route('/checkbox4', methods=['GET', 'POST'])
def checkbox4():
    if request.method == "POST":    
        if request.form.get('d_enabled') == 'on':
            print("ON")
        else:
            print("OFF")
               
    return render_template("checkbox4.htm")
#https://stackoverflow.com/questions/54972705/sending-checkbox-value-to-flask

@app.route('/checkbox3', methods=['GET', 'POST'])
def checkbox3():
    if request.method == "POST":
        if request.form['submit'] == 'submit':
            print(request.form.get('check'))
               
    return render_template("checkbox3.htm")

@app.route("/led/<state>", methods=["GET", "POST"])
def _led():
    state = request.args.get('state')
    if state == "on":
        print("led on")
    else:
        print("led off")       
    return "susses"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.htm")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == "__main__":
    app.run(debug=True)