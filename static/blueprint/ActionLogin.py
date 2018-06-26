from flask import Blueprint, render_template, request, jsonify, session
from static.blueprint.TestData import testLogin

action_login = Blueprint('action_login', __name__, template_folder='templates')

@action_login.route('/tryLogin', methods=['POST'])
def tryLogin():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    # [ email, password ]
    print('Get param: {}'.format(catchData))
    is_in_db = False
    callback = []

    if catchData[0] == 'aleks@vp.pl':
        if catchData[1] == '6674192158d0ab15756bad24f2fab71f':
            is_in_db = True
    callback.append(is_in_db)
    if is_in_db:
        testLogin()
        try:
            callback.append('Logowanie powiodło się.')
            callback.append(session['user_id'])
            callback.append(session['user_email'])
            callback.append(session['user_first_name'])
            callback.append(session['user_last_name'])
        except:
            callback.append('Błąd pobrania sesji.')
            callback.append(1)
            callback.append('j.doe@gmail.com')
            callback.append('John')
            callback.append('Doe')
    else:
        callback.append('Nieprawidłowe dane logowania.')

    print(callback)
    # session.clear()
    return jsonify({'param': callback});


@action_login.route("/include_login")
def IncludeLogin():
    return render_template('include/include_login.html')


@action_login.route("/include_registry")
def IncludeRegistry():
    return render_template('include/include_registry.html')