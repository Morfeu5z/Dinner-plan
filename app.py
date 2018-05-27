from flask import Flask, render_template

# from my_app import app
app = Flask(__name__)
from log_reg import log_reg
from admin_panel import admin_panel

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


app.run(debug=True, host="127.0.0.1", port=5000)
