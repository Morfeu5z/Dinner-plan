import os

from flask import Flask, render_template, session

# from my_app import app
app = Flask(__name__)
from static.blueprint.ActionLogin import action_login
from static.blueprint.ActionAdmin import action_admin
from static.blueprint.ActionRegistry import action_registry

app.register_blueprint(action_login)
app.register_blueprint(action_registry)
app.register_blueprint(action_admin)

app.secret_key = os.urandom(24)

@app.route("/")
def home():
    '''
    Strona startowa HOME
    z konfiguracją
    :return:
    '''
    init = {
        'title': 'Dinner Plan',
        'css':'index',
        'onStart': 'login'
    }
    return render_template('index.html', init=init)


app.run(debug=True, host="127.0.0.1", port=5000)
