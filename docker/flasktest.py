import os
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime   
import socket

app = Flask(__name__)

# Vérifier si la base de données doit être utilisée
use_db = os.getenv("NO_DB") != "true"

if use_db:
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    db = client["flask_db"]
    collection = db["requests"]

# MongoDB connection
#client = MongoClient(os.getenv("MONGO_URI"))
#db = client["flask_db"]
#collection = db["requests"]

# Informations sur le projet
PROJECT_NAME = "My Project"
VERSION = "V1"
NAME = "Quentin Flamarion"

@app.route("/")
def flaskTest():
    if use_db:
        # Enregistrer la requête
        client_ip = request.remote_addr
        current_date = datetime.now()
        collection.insert_one({"ip": client_ip, "date": current_date})
        last_request = list(collection.find().sort("_id", -1).limit(1))
        return f"<h1>Flask App</h1><p>Database Connected: {use_db}</p><p>{last_request}</p>"
    return f"<h1>Flask App</h1><p>Database Connected: {use_db}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)       