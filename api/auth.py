from flask import Blueprint, request, jsonify, make_response
from helpers.db import sessionmaker, engine
from helpers.jwt import token_required
from datetime import datetime, timedelta
from orm_classes.account import Account
from secret.api import SECRET_KEY
import jwt

auth : Blueprint = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST', 'GET'])
def login():
    # get json as dict
    content : dict = request.get_json()  # type: ignore

    # ensure required keys exist
    for k in ['username', 'pwhash']:
        if k not in content:
            return jsonify({'err' : f'Required key {k} not found'}), 400

    Session = sessionmaker(bind = engine)
    session = Session()

    # query db for an account that has matching username and password hash (SHA256 or whatever)
    user : Account|None = session.query(Account)\
        .filter_by(username = content['username'])\
        .filter_by(pwhash = content['pwhash'])\
        .first()
    
    if user is None:
        return jsonify({'err' : 'User/PW error'}), 401

    # gib jwt token
    token = jwt.encode(
        {
            'userid'    :   user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, SECRET_KEY
    )

    return jsonify({'token' : token}), 201

@auth.route('/auth/signup', methods=['POST'])
def sign_up():
    content : dict = request.get_json()  # type: ignore

    for k in ['username', 'pwhash']:
        if k not in content:
            return jsonify({'err' : f'Required key {k} not found'}), 400        

    Session = sessionmaker(bind = engine)
    session = Session()

    # query db for an account that has matching username (no duplicate usernames allowed)
    user : Account|None = session.query(Account)\
        .filter_by(username = content['username'])\
        .first()            
    
    if user is not None:
        return jsonify({'err' : 'Username already exists'}), 400

    new_user : Account = Account(content['username'], content['pwhash'])
    session.add(new_user)
    session.commit()

    return jsonify(),200