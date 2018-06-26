#!/usr/bin/python3
import Data.tool.libtest
import Data.conf
from flask import Flask, render_template
from Data.tool.Arguments import Argumnets
from Data.tool.Permission import Permission
from log_reg import log_reg
from admin_panel import admin_panel



app = Flask(__name__)
app.register_blueprint(log_reg)
app.register_blueprint(admin_panel)


@app.route("/")
def home():
    init = {
        'title': 'Dinner Plan',
        'css':'index',
        'onStart': 'login',
        'js': 'registry'
    }
    return render_template('index.html', init=init)


@app.route("/panel")
def admin():
    init = {
        'title': 'Panel zarządzania',
        'css':'menu',
        'onStart': 'menu',
        'js': 'menu'
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