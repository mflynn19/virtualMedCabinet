from app import app
from flask_pymongo import PyMongo
from pymongo import MongoClient

app.config['MONGO_DBNAME'] = 'virtualMedCabinet' 
app.config['MONGO_URI'] = 'mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority'
mongo = PyMongo(app) 

client = MongoClient("mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority")
db = client['virtualMedCabinet']
collection = mongo.db.medications




