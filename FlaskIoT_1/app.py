from flask import Flask, render_template, request
#import Rasp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/_led')
def _led():
    state = request.args.get('state')
    if state == 'on':
        print("ON")
        #Rasp.LEDon()
    else:
        print("OFF")
        #Rasp.LEDoff()
    return "susses"
        
if __name__ == '__main__':
    #Rasp.conf()
    app.run(debug=True, host='0.0.0.0', port=80)
    
#https://jquerymobile.com/