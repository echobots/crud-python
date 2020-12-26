from flask import Blueprint, render_template
from ecommerce.models import General

general_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@general_bp.route('/')
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
	return render_template('general/content.html', data=jsonify(allData))

# @general_bp.route('/', methods=["GET", "POST"])
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

# @general_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)

@general_bp.route('/tambah', methods=['POST'])
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

@general_bp.route('/edit', methods=['POST'])
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

# @general_bp.route("/update", methods=["POST"])
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

@general_bp.route('/delete/<string:id_data>', methods=['GET'])
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

# @general_bp.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")