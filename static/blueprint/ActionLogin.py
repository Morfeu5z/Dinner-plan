from flask import Blueprint, render_template, request

action_login = Blueprint('action_login', __name__, template_folder='templates')

@action_login.route('/login', methods=['POST'])
def log():
    email = request.form.get('email')
    passwd = request.form.get('pass')
    return email + ' ' + passwd


@action_login.route("/include_login")
def IncludeLogin():
    return render_template('include/include_login.html')


@action_login.route("/include_registry")
def IncludeRegistry():
    return render_template('include/include_registry.html')