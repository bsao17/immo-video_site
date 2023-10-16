from flask import Blueprint, render_template
from flask_login import login_required

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder="auth")


@auth_blueprint.route('/login')
def auth_login():
    return render_template('login.html')


@auth_blueprint.route('/profile')
@login_required
def auth_profile():
    return render_template('profile.html')
