from flask import Blueprint, request, jsonify, make_response
from helpers.db import engine
from helpers.jwt import token_required, create_token, get_token_user
from datetime import datetime, timedelta
from orm_classes.account import Account
from secret.api import SECRET_KEY
from sqlalchemy.orm import sessionmaker

auth : Blueprint = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST', 'GET'])
def login():
    # get json as dict
    print(request.headers)
    print(request.data)
    content : dict = request.get_json()  # type: ignore

    # ensure required keys exist
    for k in ['username', 'pwtext']:
        if k not in content:
            return jsonify({'err' : f'Required key {k} not found'}), 400

    Session = sessionmaker(bind = engine)
    session = Session()

    # query db for an account that has matching username and password (plaintext or hashed, matching stored in db)
    user : Account|None = session.query(Account)\
        .filter_by(username = content['username'])\
        .filter_by(pwtext = content['pwtext'])\
        .first()
    
    if user is None:
        return jsonify({'err' : 'User/PW error'}), 401

    token = create_token(user.id, timedelta(minutes=30))  # type: ignore
    print(token)
    return jsonify({'token' : token}), 201  # type: ignore

@auth.route('/auth/signup', methods=['POST'])
def sign_up():
    content : dict = request.get_json()  # type: ignore

    for k in ['username', 'pwtext']:
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

    new_user : Account = Account(content['username'], content['pwtext'])
    session.add(new_user)
    session.commit()

    return jsonify(),200

@auth.route('/auth/token', methods=['POST', 'GET'])
@get_token_user
def token_refresh(user : Account):
    #print(request.headers['Authorization'])

    #identity = get_jwt_identity()
    #access_token = create_access_token(identity, expires_delta = timedelta(minutes=30))
    token = create_token(user.id, timedelta(minutes=30))  # type: ignore
    return jsonify({'token' : token}), 201  # type: ignore