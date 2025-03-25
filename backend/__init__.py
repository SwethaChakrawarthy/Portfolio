# import os
# from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import LoginManager
# # from backend.models.user import db, User
# # from flask_login import logout_user, login_required

# def create_app():
#     app = Flask(
#         __name__,
#         template_folder=os.path.join(os.pardir, 'frontend', 'templates'),
#         static_folder=os.path.join(os.pardir, 'frontend', 'static')
#     )

#     # app.config['SECRET_KEY'] = 'thisissecret'
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#     # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # db.init_app(app)

#     # login_manager = LoginManager()
#     # login_manager.login_view = 'auth.login'
#     # login_manager.init_app(app)

#     # @login_manager.user_loader
#     # def load_user(user_id):
#     #     return User.query.get(int(user_id))

#     # from .routes.auth import auth_bp
#     # from .routes.home import home_bp
#     # app.register_blueprint(auth_bp)
#     # app.register_blueprint(home_bp)

#     # with app.app_context():
#     #     db.create_all()

#     return app

import os
from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.pardir, 'frontend', 'templates'),
        static_folder=os.path.join(os.pardir, 'frontend', 'static')
    )

    # Register the home blueprint
    from .routes.home import home_bp
    app.register_blueprint(home_bp)

    return app