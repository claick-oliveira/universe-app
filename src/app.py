import os
from flask import jsonify

# App Initialization
from . import create_app  # from __init__ file
app = create_app(os.getenv("CONFIG_MODE"))


@app.route('/')
def hello():
    return jsonify({"message": "Universe API"}), 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not Found"}), 404


# Applications Routes
from .views import planets  # noqa: F401, E402
from .views import stars  # noqa: F401, E402


if __name__ == "__main__":
    app.run()
