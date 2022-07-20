from flask import Flask
from flask_cors import CORS
import jwt
from secret.api import SECRET_KEY

from api.test import testapi
from api.auth import auth

app = Flask(__name__)
app.register_blueprint(testapi)
app.register_blueprint(auth)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)

if __name__ == '__main__':
    app.run(host= '127.0.0.1',debug=True)