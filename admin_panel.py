from flask import Blueprint, render_template, request

admin_panel = Blueprint('admin_panel', __name__, template_folder='templates')

@admin_panel.route("/include_menu")
def ir():
    return render_template('include/include_menu.html')