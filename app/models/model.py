from app import app
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import Flask
from flask_googlemaps import GoogleMaps

app.config['MONGO_DBNAME'] = 'virtualMedCabinet' 
app.config['MONGO_URI'] = 'mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAeblEyV-LSsY4vuxgE8snVSc_IBj0yivM"
mongo = PyMongo(app) 

client = MongoClient("mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority")
db = client['virtualMedCabinet']
collection = mongo.db.medications




