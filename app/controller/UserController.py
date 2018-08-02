from flask import request
from app.model import db
from app.controller import app
from app.model.User import User


@app.route('/user/<name>')
def getUser(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        return 'no user'
    else:
        return "username:" + user.username + ", email:" + user.email


@app.route('/user/add')
def addUser():
    db.session.add(User(request.args.get('username'), request.args.get('email')))
    db.session.commit()
    return 'add user success'
