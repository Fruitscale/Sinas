import os
from pathlib import Path

import yaml
from flask import Blueprint, session, jsonify, make_response

from sinas.local import build_jekyll

api = Blueprint('api', __name__)


@api.route('/api/build/<path:path>')
def build(path):
    """Builds the project at `path`

    This function is intented to be used with an async REST call because the server waits until the build is done
    before returning. """
    # TODO: use the builder that is configured for the project
    # TODO: return better data
    if build_jekyll('jekyll', path, os.path.join(path, 'build')) == 0:
        return jsonify({'success': True})
    else:
        return make_response(jsonify({'success': False}), 400)


@api.route('/api/load/<path:path>')
def load(path):
    """Loads the sinas.yaml and generator config into session memory"""

    try:
        with open(os.path.join(Path.home(), path, 'sinas.yaml')) as f:
            session[path] = {'config': yaml.load(f.read())}
        if session[path]['config']['generator'] == 'jekyll':
            with open(os.path.join(Path.home(), path, '_config.yml')) as f:
                session[path]['generator_config'] = yaml.load(f.read())
        return jsonify({'success': True})
    except KeyError as e:
        return make_response(jsonify({'success': False, 'error': 'malformed_config'}), 400)
    except yaml.YAMLError as e:
        return make_response(jsonify({'success': False, 'error': 'parse_error'}), 400)
    except FileNotFoundError as e:
        return make_response(jsonify({'success': False, 'error': 'not_found'}), 404)
