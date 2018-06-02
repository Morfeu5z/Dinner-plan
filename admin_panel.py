from flask import Blueprint, render_template, request

admin_panel = Blueprint('admin_panel', __name__, template_folder='templates')

@admin_panel.route("/include_menu")
def menu():
    data = {
        'status':'Administrator',
        'user':'Aleksander Sinkowski'
    }
    return render_template('include/include_menu.html', init = data)

@admin_panel.route("/include_zapisani")
def listOfsaved():
    return render_template('include/include_zapisani.html')