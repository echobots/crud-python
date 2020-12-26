#!/usr/bin/env python3
from flask import (
	Flask, render_template, request, redirect, url_for, jsonify, make_response, abort
)
from flask_cors import CORS
from flask_mysqldb import MySQL
# import pymysql
import yaml
# import datetime
# import psycopg2

from ecommmerce.api.api import api_bp
from ecommmerce.auth.auth import auth_bp
from ecommmerce.general.general import general_bp

# import os
# from flask_sqlalchemy import SQLAlchemy

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
# app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
# app.secret_key = os.urandom(24)
# app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@Naufaldb123@localhost/startup"
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:orinest@ip:port/database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = yaml.load(open('database.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['pass']
app.config['MYSQL_DB'] = db['db']

# db = SQLAlchemy(app)
mysql = MySQL(app)
CORS(app)

# # config
# conn = pymysql.connect(host='localhost', user='root', password='', db='blog')
# cur = conn.cursor()

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)

if __name__ == "__main__":
	app.run(port='5000', debug=True)