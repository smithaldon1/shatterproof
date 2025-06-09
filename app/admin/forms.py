from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length

class EventForm(FlaskForm):
    venue = StringField('Venue')
    city = StringField('City, State')
    date = DateTimeField('Month DD, YYYY 00:00PM')
    fblink = StringField('Facebook Link')
    submit = SubmitField('Add Event')