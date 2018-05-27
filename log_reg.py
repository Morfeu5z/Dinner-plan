from flask import Blueprint, render_template, request

log_reg = Blueprint('log_reg', __name__, template_folder='templates')

@log_reg.route('/login', methods=['POST'])
def log():
    email = request.form.get('email')
    passwd = request.form.get('pass')
    return email + ' ' + passwd


@log_reg.route('/registry', methods=['POST'])
def reg():
    email = request.form.get('email')
    passwd = request.form.get('pass1')
    return email + ' ' + passwd


@log_reg.route("/include_login")
def il():
    return render_template('include/include_login.html')


@log_reg.route("/include_registry")
def ir():
    return render_template('include/include_registry.html')