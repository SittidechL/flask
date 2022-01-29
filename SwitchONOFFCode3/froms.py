from flask_wtf import FlaskForm
from wtforms import SubmitField

class PowerSwitchForm(FlaskForm):
    power_switch = SubmitField("ON")