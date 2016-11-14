from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_nav import Nav
from flask import Blueprint

from db import init, Session
import mappings
import frontend
from nav import nav


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.db = init()
    app.register_blueprint(frontend.frontend)
    nav.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
