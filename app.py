from typing import Any

from flask import Flask

from views import main_bp


def create_app() -> Any:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
