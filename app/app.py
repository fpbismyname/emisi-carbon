from flask import Flask
from app.route import route

def create_app():
    app = Flask(__name__)
    route(app).routes()
    return app