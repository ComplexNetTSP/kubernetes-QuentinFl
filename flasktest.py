from flask import Flask
from datetime import datetime   
import socket

app = Flask(__name__)

# Informations sur le projet
PROJECT_NAME = "My Project"
VERSION = "V1"

@app.route("/")
def flaskTest():
    name = "Quentin Flamarion"
        # Obtenir le nom d'hôte du serveur
    server_hostname = socket.gethostname()
    # Obtenir la date actuelle
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Retourner les informations dans la réponse HTML
    return f"""
    <html>
        <head>  
            <title>{PROJECT_NAME}</title>
        </head>
        <body>
            <h1>{name}'s Website</h1>
            <h1>Project Name:</strong> {PROJECT_NAME}</h1>
            <p>Version: {VERSION}</p>
            <p>Server Hostname: {server_hostname}</p>
            <p>Current Date: {current_date}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)