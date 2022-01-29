#https://stackoverflow.com/questions/51057966/flask-toggle-button-with-dynamic-label
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import PowerSwitchForm

@app.route('/power', methods=['GET', 'POST'])
def power():
  power_switch = PowerSwitchForm()
  if power_switch.power_switch.label.text == "ON" and power_switch.validate():
    flash("Power has been turned ON")
    power_switch.power_switch.label.text = "OFF"
    return redirect(url_for('power'))
  elif power_switch.power_switch.label.text == "OFF" and power_switch.validate():
    flash("Power has been turned OFF")
    power_switch.power_switch.label.text = "ON"
    return redirect(url_for('power'))
  return render_template('power.html', form0=power_switch)