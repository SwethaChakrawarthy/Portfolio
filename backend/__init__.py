
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