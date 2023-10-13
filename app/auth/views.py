from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/login')
def auth_login():
    return render_template('auth/login.html')


@auth_blueprint.route('/logout')
def auth_logout():
    return render_template('auth/logout.html')
