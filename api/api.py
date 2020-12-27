from flask import Blueprint, render_template
from ecommerce.models import *

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/users')
def getUsers():
	all_data = Users.query.all()
	return jsonify(all_data)