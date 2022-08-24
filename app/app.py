from flask import Flask
from app.setting import ProdConfig
from flask import Blueprint
from app.api import routes as api_bp


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)
    #register_env(app)
    # register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    return app

# def register_env(app):
#     DATABAS

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(api_bp.blueprint)