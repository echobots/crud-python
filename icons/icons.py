from flask import Blueprint

icons_bp = Blueprint('icons_bp', __name__,
    static_folder='static',
    static_url_path='icons')