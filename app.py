from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This turn off the flask SQLAlchemy modification tracker because SQLAlchemy has its own.
app.secret_key = 'jose'
api = Api(app)



# https://blog.tecladocode.com/learn-python-advanced-configuration-of-flask-jwt/
#app.config["JWT_AUTH_URL_RULE"] = '/login'
jwt = JWT(app,authenticate,identity) # create new endpoint /auth
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

#@jwt.auth_response_handler
#def customized_response_handler(access_token, identity):
#    return jsonify({
#                        'access_token': access_token.decode('utf-8'),
#                        'user_id': identity.id
#                   })


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')

#from db import db
#db.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, port=5000)

