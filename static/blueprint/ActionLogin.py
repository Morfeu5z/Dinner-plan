from flask import Blueprint, render_template, request, jsonify

action_login = Blueprint('action_login', __name__, template_folder='templates')

@action_login.route('/tryLogin', methods=['POST'])
def tryLogin():
    catchData = request.get_json(force=True)
    catchData = catchData['param']
    # [ email, password ]
    print('Get param: {}'.format(catchData))
    is_in_db = False
    if catchData[0] == 'aleks@vp.pl' and catchData[1] == '6674192158d0ab15756bad24f2fab71f':
        is_in_db = True
    callback = [is_in_db, 'Serwer response.']
    print(callback)
    return jsonify({'param': callback});


@action_login.route("/include_login")
def IncludeLogin():
    return render_template('include/include_login.html')


@action_login.route("/include_registry")
def IncludeRegistry():
    return render_template('include/include_registry.html')