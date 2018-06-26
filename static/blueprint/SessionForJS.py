from time import sleep
from flask import Blueprint, request, session, jsonify

session_for_js = Blueprint('session_for_js', __name__, template_folder='templates')


@session_for_js.route('/sessionControler', methods=['POST'])
def sessionControler():
    '''
        Session:
        * Add
        * Update
        * Get
        * Delete
        :param set name of session
        :param set value in to session
        :return get value from session
    '''
    print("Wywolano session flask.")
    if request.form.get('action') == 'clear':
        session.clear()
        print('Session is clear')
        return jsonify({'param': 'Session Clear'})

    if request.form.get('action') == 'set':
        name = request.form.get('name')
        param = request.form.get('param')
        session[name] = param
        print("Set session: " + name + " = " + param)
        return jsonify({'param': param})

    if request.form.get('action') == 'get':
        name = request.form.get('name')
        if name in session:
            param = session[name]
            print("Get session: " + name)
            return jsonify({'param': param})
        elif name in session:
            sleep(0.5)
            param = session[name]
            print("Get session: " + name)
            return jsonify({'param': param})
        else:
            print("Session is missing: " + name)
            return jsonify({'param': ''})