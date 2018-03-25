from flask import Flask, request
from handler.user_handler import UserHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "The beginning"

'''User Routes'''
@app.route('/QuePasApp/users')
def users():
    if request.args:
        return UserHandler().searchUserByName(request.args)
    else:
        handler = UserHandler()
        return handler.getAllUsers()

@app.route('/QuePasApp/users/<int:IdUser>')
def getUserById(IdUser):
    handler = UserHandler()
    return handler.getUserbyId(IdUser)


if __name__ == '__index__' :
    app.run()

