import os
from pathlib import Path

from flask import Blueprint, send_from_directory

from sinas.views.api import api

frontend = Blueprint('frontend', __name__, template_folder='templates')


@frontend.route('/')
def home():
    return "This is the home page!", 200


@frontend.route('/projects/<path:path>/build/<path:file>')
def live(path, file):
    """Views the latest build of the project at `path`"""
    return send_from_directory(os.path.join(Path.home(), path, 'build'), file)
