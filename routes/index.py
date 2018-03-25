from flask import Flask, request
from handler.user_handler import UserHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "The beginning"

'''User Routes'''
@app.route('/QuePasApp/users')
def users():
    handler = UserHandler()
    return handler.getAllUsers()

if __name__ == '__index__' :
    app.run()

