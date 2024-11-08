from flask import Flask
from app.route import Routes

def create_app():
    app = Flask(__name__)
    
    Routes(app=app)
    
    return app