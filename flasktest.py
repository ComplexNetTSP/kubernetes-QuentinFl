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
client = MongoClient(os.getenv("MONGO_URI"))
db = client["flask_db"]
collection = db["requests"]

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
    return f"<h1>Flask App</h1><p>Database Connected: {use_db}</p>"

##Challenge 3 below
 # Récupérer les 10 derniers enregistrements
    last_10_requests = list(collection.find().sort("_id", -1).limit(10))

    server_hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    responses = ""
    
    for req in last_10_requests:
        responses += f"<li>{req['ip']} - {req['date']}</li>"

    # Retourner les informations dans la réponse HTML
    response = f"""
    <html>
        <head>  
            <title>{PROJECT_NAME}</title>
        </head>
        <body>
            <h1>{NAME}'s Website</h1>
            <h1>Project Name:</strong> {PROJECT_NAME}</h1>
            <p>Version: {VERSION}</p>
            <p>Server Hostname: {server_hostname}</p>
            <p>Current Date: {current_date}</p>
            <ul>
            {responses}
            </ul> 
        </body>
        
    </html>
    """

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)       