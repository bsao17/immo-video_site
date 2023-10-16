from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder="auth")


@auth_blueprint.route('/login')
def auth_login():
    return render_template('login.html')


@auth_blueprint.route('/logout')
def auth_logout():
    return render_template('logout.html')
