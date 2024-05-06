from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

import strings
from config import Config

login = LoginManager()
db = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize extensions
    login.init_app(app)
    login.login_view = "auth.login"
    db.init_app(app)
    bootstrap.init_app(app)

    # register blueprints
    from L3_web.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from L3_web.home import bp as home_bp
    app.register_blueprint(home_bp)

    @app.context_processor
    def inject_session_keys():
        return {"strings": strings}

    # app context needed
    with app.app_context():
        db.create_all()

    return app
