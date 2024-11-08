def Routes(app):
    app = app
    
    """

        #Routes

        Example Routes
        @app.route("/")
        def index():
            return "Home"
            
    """
    
    # Routes here
    @app.route("/")
    def index():
        return "index"
    
    @app.route("/home")
    def home():
        return "home"