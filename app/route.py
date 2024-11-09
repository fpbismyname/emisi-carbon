# Import controller
from app.controllers.userController import userController

# Routes
class route:
    def __init__(self, flaskApp) -> None:
        # register flaskapp
        self.app = flaskApp
        #register controller
        self.userController = userController
    
    def routes(self):
        app = self.app
        
        @app.route('/', methods=['GET'])
        def index():
            return "Testing done"