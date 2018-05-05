from flask import request, jsonify, Blueprint
from my_app import app, db
from my_app.Catalog.Model import User

catalog = Blueprint('catalog', __name__)


@catalog.route("/")
@catalog.route("/home")
def home():
    return "Welcome to the Catalog Home"


@catalog.route("/user/<email>")
def user(email):
    user = User.query.get_or_404("email")
    return 'Users - %s, %s, %s' % (user.email, user.name, user.surname)


@catalog.route("/users")
def users():
    users = User.query.all()
    res = {}
    for user in users:
        res[user.id] = {
            'name' : user.name,
            'email': user.email,
            'surname': user.surname
        }
    return jsonify(res)


@catalog.route("/user-create", method=['Post',])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    surname = request.form.get('surname')
    user = User(email, name, surname)
    db.session.add(user)
    db.session.commit()
    return 'Product Created'