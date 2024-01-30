from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm(FlaskForm):
    '''defines fields for new pet form'''

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", default=True, validators=[Optional()])