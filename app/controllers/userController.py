# Import Models
from app.models.UserModels import UserModels

class userController:
    userModels = None
    
    def __init__(self):
        self.user = ["Fajar", "fajar123"]
        self.userModels = UserModels
    
    @staticmethod
    def getUsers(self, username:any, password:any):
        return self.UserModel.getUser(username="Fajar", password="Fajar123")