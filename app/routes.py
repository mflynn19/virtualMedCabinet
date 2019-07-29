from app import app
from flask import render_template, request
from app.models import model, formopener
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = 'virtualMedCabinet' 
app.config['MONGO_URI'] = 'mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority'
mongo = PyMongo(app) 

@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/addNew')
def addNew():
    return render_template("addNew.html")
    
@app.route('/yourMeds', methods = ['GET', 'POST'])
def yourMeds():
    if request.method == 'POST':
        formData = dict(request.form)
        collection = mongo.db.medications
        collection.insert({"name": formData["medName"], "purpose":formData["medPurpose"], "doc":formData["doctor"], "amount":formData["medCount"], "type":formData["medType"]})
        collection = list(collection.find({}))
        return render_template("yourMeds.html", collection=collection)
    else:
        return render_template("yourMeds.html")
