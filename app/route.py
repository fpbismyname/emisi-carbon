from flask import Flask

def create_app():
    app = Flask(__name__)
    
    def home():
        return "Homa"
    
    app.add_url_rule("/", "home", home)
    return app