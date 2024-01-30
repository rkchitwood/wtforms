# ## **Step 1: Create Database & Model**

# Create a Flask and Flask-SQLAlchemy project, “adopt”.

# Create a single model, ***Pet***. This models a pet potentially available for adoption:

# - ***id***: auto-incrementing integer
# - ***name***: text, required
# - ***species***: text, required
# - ***photo_url***: text, optional
# - ***age***: integer, optional
# - ***notes***: text, optional
# - ***available***: true/false, required, should default to available

# While setting up the project, add the Debug Toolbar.

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
default_photo = 'https://clipart-library.com/images/pco5rbqcE.jpg'

def connect_db(app):
    '''connects to database and creates tables if not created'''
    db.app=app
    db.init_app(app)
    #db.drop_all()
    db.create_all()

class Pet(db.Model):
    '''the table for pets'''

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = False, default = default_photo)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)

