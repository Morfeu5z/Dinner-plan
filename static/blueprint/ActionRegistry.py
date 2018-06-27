from flask import Blueprint, render_template, request, jsonify, session, redirect
from Data.database.controllers.UserController import UserController

action_registry = Blueprint('action_registry', __name__, template_folder='templates')

@action_registry.route('/registry', methods=['POST'])
def registry_action():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    # [ 0 : first_name, 1 : last_name, 2 : email, 3 : password_1, 4 : password_2 ]
    # print('Get param: {}'.format(catchData))
    is_in_db = False
    message = 'Rejsetracja nie powiodła się.'
    if catchData[3] == catchData[4]:
        print('Password: OK')
        Dater = UserController()
        userData = Dater.regestration(email=catchData[2], name=catchData[0], lastname=catchData[1], password=catchData[3])
        print('Registry: OK')
        print(userData.id, userData.name, userData.lastname, userData.email, userData.permission)
        is_in_db = True if userData else False

    if is_in_db:
        print('Registry: {}'.format(is_in_db))
        # testLogin()
        session['user_id'] = userData.id
        session['user_premission'] = userData.permission
        session['user_email'] = userData.email
        session['user_first_name'] = userData.name
        session['user_last_name'] = userData.lastname
        message = 'Rejestracja udana!'

    print('Create callback')
    callback = jsonify({'param' : [is_in_db, message]})
    return callback