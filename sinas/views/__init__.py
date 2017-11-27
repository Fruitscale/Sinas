import os
from pathlib import Path

from flask import Blueprint, send_from_directory

from sinas.local import build_jekyll

frontend = Blueprint('frontend', __name__, template_folder='templates')
api = Blueprint('api', __name__)


@frontend.route('/')
def home():
    return "This is the home page!", 200


@frontend.route('/projects/<path:path>/build/<path:file>')
def live(path, file):
    """Views the latest build of the project at `path`"""
    return send_from_directory(os.path.join(Path.home(), path, 'build'), file)


@api.route('/api/build/<path:path>')
def build(path):
    """Builds the project at `path`

    This function is intented to be used with an async REST call because the server waits until the build is done
    before returning. """
    # TODO: use the builder that is configured for the project
    # TODO: return better data
    if build_jekyll('jekyll', path, os.path.join(path, 'build')) == 0:
        return 'OK', 200
    else:
        return 500
