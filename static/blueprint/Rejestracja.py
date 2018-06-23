from flask import Blueprint, render_template, request, jsonify

sign_up = Blueprint('sign_up', __name__, template_folder='templates')

@sign_up.route('/registry', methods=['POST'])
def registry_action():
    # TODO Ajax wysyła dane ale nie zostają one odebrane
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    print('Od ajaxa: '.format(catchData))
    callback = jsonify({'param' : ['Serwer take data']})
    return callback