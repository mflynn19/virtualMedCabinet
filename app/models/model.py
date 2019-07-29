from app import app
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = 'virtualMedCabinet' 
app.config['MONGO_URI'] = 'mongodb+srv://admin:Hjrf6Twqr304AJHq@cluster0-3hcwl.mongodb.net/virtualMedCabinet?retryWrites=true&w=majority'
mongo = PyMongo(app) 

def pillTaken(supply, dose):
    return supply - dose
    
def refill(oldSupply, newSupply):
    return oldSupply + newSupply
    
#def delete(medication):
    #db.collection.remove({})