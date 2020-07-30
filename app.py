from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response, abort
from flask_cors import CORS
from flask_mysqldb import MySQL
# import pymysql
import yaml
# import datetime
# import psycopg2

# import os
# from flask_sqlalchemy import SQLAlchemy

# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:orinest@ip:port/database'

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

# class Book(db.Model):
#     title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True) # db.Integer(), db.Boolean(), db.DateTime(), db.Binary()

#     def __repr__(self):
#         return "<Title: {}>".format(self.title)

# class Pekerjaan(db.Model):
#     __tablename__='pekerjaan'
#     __table_args__ = {'schema': 'hr'}
#     kodepekerjaan = db.Column(db.String(), primary_key=True)
#     namapekerjaan = db.Column(db.String())
#     kodedivisi = db.Column(db.String())
#     keterangan = db.Column(db.String())
#     hakakses = db.Column(db.String())

#     def __init__(self, kodepekerjaan, namapekerjaan, kodedivisi, keterangan, hakakses):
#         self.kodepekerjaan = kodepekerjaan
#         self.namapekerjaan = namapekerjaan
#         self.kodedivisi = kodedivisi
#         self.keterangan = keterangan
#         self.hakakses = hakakses
    
#     def __repr__(self):
#         return '<Pekerjaan %r>' % self.kodepekerjaan

@app.route('/')
def home():
# 	query = "select * from `data`"
# 	cur.execute(query)
# 	data = cur.fetchall()
# 	for lala in data:
# 		print(lala[2])
	cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM data')
        users = cursor.fetchall()
        allData = []

        for i in users:
            id = i[0]
            name = i[1]
            age = i[2]
            dataDict = {
                "id": id,
                "name": name,
                "age": age
            }
            allData.append(dataDict)
	return render_template('content.html', data=jsonify(allData))

# @app.route('/', methods=["GET", "POST"])
# def home():
#     books = None
#     if request.form:
#         try:
#             book = Book(title=request.form.get("title"))
#             db.session.add(book)
#             db.session.commit()
#         except Exception as e:
#             print("Failed to add book")
#             print(e)
#     books = Book.query.all()
#     return render_template("home.html", books=books)

@app.route('/tambah', methods=['POST'])
def tambah():
# 	title = request.form['title']
# 	body = request.form['body']
# 	query = "insert into `data` (title, body) values ('{0}','{1}')".format(title, body)
# 	cur.execute(query)
# 	conn.commit()
	body = request.form
        name = body['name']
        age = body['age']

        cursor = mysql.connection.cursor()
        cursor.execute(f'INSERT INTO data VALUES(null, { str(name) }, { str(age) })')
        mysql.connection.commit()
        cursor.close()
        print(jsonify({
            'status': 'Data is posted to MySQL!',
            'name': name,
            'age': age
        }))
	return redirect(url_for('home'))

@app.route('/edit', methods=['POST'])
def edit():
# 	id_data = request.form['id']
# 	title = request.form['title']
# 	body = request.form['body']
# 	query = "UPDATE data SET title='{1}', body='{2}' WHERE id={0}".format(id_data, title, body)
# 	cur.execute(query)
# 	conn.commit()
	
	body = request.form
        name = body['name']
        age = body['age']

        cursor = mysql.connection.cursor()
        cursor.execute(f'UPDATE data SET title='{ id_data }', body='{ title }' WHERE id={ body }')
        mysql.connection.commit()
        cursor.close()
        print(jsonify({'status': 'Data '+id+' is updated on MySQL!'}))
	return redirect(url_for('home'))

# @app.route("/update", methods=["POST"])
# def update():
#     try:
#         newtitle = request.form.get("newtitle")
#         oldtitle = request.form.get("oldtitle")
#         book = Book.query.filter_by(title=oldtitle).first()
#         book.title = newtitle
#         db.session.commit()
#     except Exception as e:
#         print("Couldn't update book title")
#         print(e)
#     return redirect("/")

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
# 	query = "DELETE from `data` where id={0}".format(id_data)
# 	cur.execute(query)
# 	conn.commit()

        cursor = mysql.connection.cursor()
        cursor.execute(f'DELETE from `data` where id={ id_data }')
        mysql.connection.commit()
        cursor.close()
        print(jsonify({'status': 'Data '+id+' is deleted on MySQL!'}))
	return redirect(url_for('home'))

# @app.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
