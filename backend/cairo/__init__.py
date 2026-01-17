from cairo import models
from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @app.get("/health")
    def health():
        return jsonify(status="ok", app="cairo")

    return app
