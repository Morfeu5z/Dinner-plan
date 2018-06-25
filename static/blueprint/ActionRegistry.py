from flask import Blueprint, render_template, request, jsonify

action_registry = Blueprint('action_registry', __name__, template_folder='templates')

@action_registry.route('/registry', methods=['POST'])
def registry_action():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    # [ 0 : first_name, 1 : last_name, 2 : email, 3 : password_1, 4 : password_2 ]
    # print('Get param: {}'.format(catchData))
    if catchData[3] == catchData[4]:
        print('Password: OK')
    callback = jsonify({'param' : ['Serwer take data']})
    return callback