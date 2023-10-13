from flask import render_template, Blueprint, Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route('/')
def index():
    return render_template('index.html')