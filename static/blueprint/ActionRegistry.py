from flask import Blueprint, render_template, request, jsonify

action_registry = Blueprint('action_registry', __name__, template_folder='templates')

@action_registry.route('/registry', methods=['POST'])
def registry_action():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    print('Get param: {}'.format(catchData))
    print('Wywołano żadanie ajaxem')
    callback = jsonify({'param' : ['Serwer take data']})
    return callback