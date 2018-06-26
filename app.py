#!/usr/bin/python3
# import Data.tool.libtest
import Data.conf
from Data.tool.Arguments import Argumnets
from Data.tool.Permission import Permission

import os
from flask import Flask, render_template, session

from static.blueprint.ActionLogin import action_login
from static.blueprint.ActionAdmin import action_admin
from static.blueprint.ActionRegistry import action_registry
from static.blueprint.SessionForJS import session_for_js


app = Flask(__name__)
app.register_blueprint(action_login)
app.register_blueprint(action_registry)
app.register_blueprint(action_admin)
app.register_blueprint(session_for_js)

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


@Argumnets.Host
@Permission.login
def run(debug, host, port):
    # starting server and configuration
    # system variables with test decor-
    # ators, which ask script exc para-
    # meters and test on connect to the
    # database
    #
    # Parameters by default
    # :host: 0.0.0.0
    # :port: 5000
    # :debug: True
    app.run(debug=debug, host=host, port=port)
    return 0

run()