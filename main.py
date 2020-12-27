from flask import (
	Flask, request, redirect, url_for, jsonify, make_response, abort
)
from flask_cors import CORS
import os, datetime, pymysql # psycopg2
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL

from ecommerce.api.api import api_bp
from ecommerce.auth.auth import auth_bp
from ecommerce.general.general import general_bp

app = Flask(__name__)
# app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

#SqlAlchemy Database Configuration With Mysql or Postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@Naufaldb123@localhost/startup" # 'postgresql+psycopg2://postgres:password@ip:port/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlite
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# import database conf
# import yaml
# db = yaml.safe_load(open('database.yaml'))

app.logger.setLevel(10)
app.config.update({
	'DEBUG': True,
	'APP_NAME': __name__,
	'SECRET_KEY': 'Secret Key', # os.urandom(24)
	'JSONIFY_MIMETYPE': 'application/json;charset=UTF-8',
})

db = SQLAlchemy(app)
# mysql = MySQL(app)
# CORS(app)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)