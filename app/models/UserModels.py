class UserModels:
    
    accounts = []
    
    def __init__(self):
        accounts = [{
            "id": 1,
            "username": "Fajar",
            "password": "Fajar123"
        }]
        self.accounts = accounts
    
    @staticmethod
    def getUser(self, username = None, password = None):
        for account in self.accounts:
            if account['username'] == username and account['password'] == password:
                return "Account Finded"
            else:
                return "Account Not Found, are you hack someone ?"