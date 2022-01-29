#https://www.py4u.net/discuss/273669
from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def change():
    if request.method == 'POST':
        spkrs_00 = request.form.getlist('spkrs-00')
        spkrs_01_state = request.args['spkrs-01']
        spkrs_02_state = request.args['spkrs-02']
        protection_state = request.args['protection']
        speakers_states = [spkrs_00, spkrs_01_state, spkrs_02_state, protection_state]
        return render_template('index.htm', speaker_states=speakers_states)
    else:
        return render_template('index.htm')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)