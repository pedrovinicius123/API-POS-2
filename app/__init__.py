from flask import Flask, jsonify
from .config import Config
from .extensions import marsh, db, migrate
from .utils.response import error_response
from .routes.messages import messages_bp
from .routes.users import user_bp
from marshmallow import ValidationError


# APP CONFIGURATIONS AND EXTENSIONS
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    marsh.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(ValidationError)
    def validation_error(err):    
        return jsonify(error_response(err))
    
    @app.errorhandler(404)
    def error_404(err):
        return jsonify(error_response(err, 404))
    
    app.register_blueprint(messages_bp)
    app.register_blueprint(user_bp)
    return app
