from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from flask_jwt_extended import JWTManager
from security import authenticate, identity
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'aoigKYKRfjofiNAJIANFapbFOAnjGASHFb;b;xz'
api = Api(app)
# jwt = JWT(app, authenticate, identity) /auth
jwt = JWTManager(app) # doesnt create /auth

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/<string:name>
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)