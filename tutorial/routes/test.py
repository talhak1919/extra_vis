from tutorial import app
from tutorial.modals.Modals import *
from flask import request

@app.route("/user",methods=["GET"])
def Post():
    users = User.query.all()
    return users

@app.route("/user",methods=["POST"])
def Post():
    data = request.json
    users = User()
    users.name = data['name']
    users.age = data['age']
    users.email = data['email']
    db.session.add(users)  # Add the user instance to the session
    db.session.commit()
    return "db updated"

@app.route("/user",methods=["PUT"])
def Put():
    data = request.json
    users = User.query.filter_by(userid=data['user_id']).first()
    users.name = data['name']
    users.age = data['age']
    users.email = data['email']
    db.session.merge(users)  # Add the user instance to the session
    db.session.commit()
    return "db updated"





    
