from datetime import timedelta, datetime
import jwt
from flask import request, jsonify
from functools import wraps
from secret.api import SECRET_KEY
from orm_classes.account import Account
from helpers.db import sessionmaker, engine

def create_token(user_id : int, expiry : timedelta) -> str:
    return jwt.encode(
        {
            'userid'    :   user_id,
            'exp' : datetime.utcnow() + expiry
        }, SECRET_KEY
    )    

def token_required(f):
    """Verifies token exist and is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # jwt is passed in the request header
        # RFC 7235: Should conform to format Authorization : Bearer <TOKEN>
        try:
            token : str = request.headers['Authorization'].split(' ')[1]
            print(token)
        except Exception as e:
            print(e)
            return jsonify({'err' : 'Missing JWT token'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print(data)

            Session = sessionmaker(bind = engine)
            session = Session()
            user : Account|None = session.query(Account)\
                .filter_by(id = data['userid'])\
                .first()

            if user is None:
                return  jsonify(
                    err='User not found'
                ), 401

        except Exception as e:
            print(e)
            return jsonify({
                'err' : 'Invalid JWT Token'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(*args, **kwargs)
  
    return decorated

def get_token_user(f):
    """ Verifies that token is valid, and returns user as Account object.
        Decorated classs must accept Account as a parameter.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # jwt is passed in the request header
        # RFC 7235: Should conform to format Authorization : Bearer <TOKEN>
        try:
            token : str = request.headers['Authorization'].split(' ')[1]
            print(token)
        except Exception as e:
            print(e)
            return jsonify({'err' : 'Missing JWT token'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print(data)

            Session = sessionmaker(bind = engine)
            session = Session()
            user : Account|None = session.query(Account)\
                .filter_by(id = data['userid'])\
                .first()

            if user is None:
                return  jsonify(
                    err='User not found'
                ), 401

        except Exception as e:
            print(e)
            return jsonify({
                'err' : 'Invalid JWT Token'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(user, *args, **kwargs)
  
    return decorated