from flask import Flask,request,render_template
import os
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/_red")
def _led():
    state = request.args.get("state")
    s={
        "led":state
    }
    fname = os.path.join(app.static_folder, "sample.json")

    with open(fname, "w") as outfile:
        json.dump(s, outfile)
    return "success"

@app.route("/read")
def redJSON(): 
    fname = os.path.join(app.static_folder, "sample.json")
    with open(fname, "r") as openfile:
        json_obj = json.load(openfile)
    return json_obj['led']

if __name__ == "__main__":
    app.run(host="192.168.1.105",port=5000)
    

#https://www.youtube.com/watch?v=gAzA19FYfsU
    
