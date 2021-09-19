from flask import Flask, render_template, redirect, request, jsonify 
from pymongo import MongoClient 
from flask_cors import CORS
import json

app = Flask(__name__)
app = Flask(__name__, template_folder='templates/', static_folder='static/', static_url_path="")
cors = CORS(app, resources={r"/*": {"origins": "*"}})
    
app.config.update(dict(SECRET_KEY='a-secret-key'))


client = MongoClient("mongodb+srv://admin:adminpa$$@cluster0.mw1sa.mongodb.net/HackRice11?retryWrites=true&w=majority")
db = client.HackRice11

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

def check_or_insert(name, password):
    print("-----------------")
    if db.Vendors.find({'name': name}).count() <= 0:
        print("vendor_id Not found, creating....")
        print(name, password)
        db.Vendors.insert({'name':name, 'password':password})

@app.route("/register/")
def render_registrazione() -> "html":
    return render_template("index.html")

@app.route('/register/', methods=['GET','POST'])
def user_registration():
    name = request.json.get('name')
    password = request.json.get('password')
    check_or_insert(name, password)
    return render_template('index.html')
    

@app.route("/")
def hello_world():
    return render_template('index.html')
    

if __name__ == "__main__":
    hello_world()