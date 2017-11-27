from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    from sinas.views import frontend
    app.register_blueprint(frontend)

    from sinas.views import api
    app.register_blueprint(api)

    return app
