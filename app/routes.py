from app import app
from flask import render_template, request
from app.models import model, formopener
from flask_pymongo import PyMongo
from flask import Flask
from flask_googlemaps import GoogleMaps

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
        meds = list(collection.find({}))
        return render_template("yourMeds.html", meds = meds)
    else:
        collection = mongo.db.medications
        meds = list(collection.find({}))
        return render_template("yourMeds.html", meds = meds)

@app.route('/adjustMed', methods = ['GET', 'POST'])
def adjustMed():
    if request.method == 'POST':
        formData = dict(request.form)
        collection = mongo.db.medications
        collection.replace_one({"name": formData["drugName"]}, {"name": formData["drugName"], "purpose":formData["drugPurpose"], "doc":formData["drugDoctor"], "amount":formData["drugAmount"], "type":formData["drugType"]})
        meds = list(collection.find({}))
        return render_template("adjustMed.html", meds = meds)
    else:
        collection = mongo.db.medications
        meds = list(collection.find({}))
        return render_template("adjustMed.html", meds = meds)
        
@app.route('/pharmacyLocator', methods = ['GET', 'POST'])
def pharmacyLocator():
    if request.method == 'POST':
        formStuff = dict(request.form)
        collection = mongo.db.zipCodes
        collection.insert({"zipCode": formStuff["zipCode"]})
        zippy = list(collection.find({}))
        return render_template("pharmacyLocator.html", zippy = zippy)
    else:
        collection = mongo.db.medications
        zippy = list(collection.find({}))
        return render_template("pharmacyLocator.html", zippy = zippy)
        
#get object id to query DB, jinja2{{}} teplate to set values based on key ({{data.doctor}}), post request to update entry for everything; update({{what to find in db}}, {{field to update use from form}}) collection.find_one_and_update gets the first instance and updates find_one({'_id': ObjectId(string version of ID)})