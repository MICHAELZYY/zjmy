from flask import Flask


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from backend.blueprints.index import index_bp
    app.register_blueprint(index_bp)
