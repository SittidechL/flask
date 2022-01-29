from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def on():
    return render_template("checkbox.htm")

if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch?v=R6ODcr-MwKE
#https://www.youtube.com/watch?v=WteIH6J9v64&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=10