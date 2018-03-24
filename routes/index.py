from flask import Flask, request

@app.route('/')
def home():
    return "The beginning";

