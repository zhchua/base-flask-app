import jwt
from flask import request, jsonify
from functools import wraps
from secret.api import SECRET_KEY
from orm_classes.account import Account

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'err' : 'Missing JWT token'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY)
            current_user = Account.query\
                .filter_by(id = data['userid'])\
                .first()
        except Exception as e:
            return jsonify({
                'err' : 'Invalid JWT Token'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated