from flask import Blueprint, render_template, request, jsonify, session, redirect
from static.blueprint.TestData import testLogin
from Data.database.controllers.UserController import UserController

action_login = Blueprint('action_login', __name__, template_folder='templates')

@action_login.route('/tryLogin', methods=['POST'])
def tryLogin():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    # [ email, password ]
    print('Get param: {}'.format(catchData))
    is_in_db = False
    callback = []

    Dater = UserController()
    userData = Dater.login(catchData[0],catchData[1])

    is_in_db = True if userData else False
    callback.append(is_in_db)

    if is_in_db:
        # testLogin()
        session['user_id'] = userData.id
        session['user_premission'] = userData.id_permission
        session['user_email'] = userData.email
        session['user_first_name'] = userData.name
        session['user_last_name'] = userData.lastname
        try:
            callback.append('Logowanie powiodło się.')
            callback.append(session['user_id'])
            callback.append(session['user_premission'])
            callback.append(session['user_email'])
            callback.append(session['user_first_name'])
            callback.append(session['user_last_name'])
        except:
            callback.append('Błąd pobrania sesji.')
            callback.append(1)
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
    if 'user_premission' in session:
        return redirect('/include_menu')
    return render_template('include/include_login.html')


@action_login.route("/include_registry")
def IncludeRegistry():
    return render_template('include/include_registry.html')