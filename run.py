from app.views import app
from app.auth.views import auth_blueprint
from app.views import main_blueprint
from config import Config

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
