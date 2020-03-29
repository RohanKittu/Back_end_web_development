#Packages used for the project.
import requests
import json
from flask import Flask,request,jsonify
import psycopg2
from flask_sqlalchemy import SQLAlchemy
import os

#initializing the flask app.
app = Flask(__name__)

#setting the url for the database.
POSTGRES_URL = "postgres://ebihzwioyypuwv:524d5f24ed074b45e81417a85b98b964a6324567e9f79ee45b237dc4fde9aba2@ec2-174-129-33-13.compute-1.amazonaws.com:5432/d5gmc7pj4k9gh"
POSTGRES_USER = "ebihzwioyypuwv"
POSTGRES_PW = "524d5f24ed074b45e81d417a85b98b964a6324567e9f79ee45b237dc4fde9aba2"
POSTGRES_DB = "d5gmc7pj4k9gh"
'''
#function for extracting env variable
def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable(POSTGRES_URL)
POSTGRES_USER = get_env_variable(POSTGRES_USER)
POSTGRES_PW = get_env_variable(POSTGRES_PW)
POSTGRES_DB = get_env_variable(POSTGRES_DB)
'''
#DB url
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

#connecting to the database 
app.config['SQLALCHEMY_DATABASE_URI'] =  DB_URL
db = SQLAlchemy(app)
#checking the connectivity of the database
if(db):
    print("connected")
else:
    print("disconnected")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/")
def home():
    return "hello"
'''