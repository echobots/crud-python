from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class General(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	id_user = db.Column(db.String(11))
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))
	lastlogin = db.Column(db.DateTime)
	template = db.Column(db.Integer)

	def __init__(self, id_user, username, password):
		# self.id = id
		self.id_user = id_user
		self.username = username
		self.password = password

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