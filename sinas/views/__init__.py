from flask import Blueprint

frontend = Blueprint('frontend', __name__, template_folder='templates')


@frontend.route('/')
def home():
    return "This is the home page!", 200
