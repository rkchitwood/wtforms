from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app=Flask(__name__)
app.config['SECRET_KEY']='key'
debug=DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO'] = True

def initialize():
    '''initializes the connection to database'''
    with app.app_context():
        connect_db(app)

initialize()

@app.route('/')
def home():
    '''returns homepage, listing pets'''

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_form():
    '''renders form to add new pet and handles submission'''
    
    form = PetForm()
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if photo_url == "": 
            photo_url = None
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:id>', methods=['GET', 'POST'])
def show_details_and_edit_form(id):
    '''renders pet details and edit form, handles form submission'''

    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        if pet.photo_url == "": 
            pet.photo_url = None
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('details_and_edit_form.html', form=form, pet=pet)
