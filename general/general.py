from flask import Blueprint, render_template
from ecommerce.models import General
from ecommerce.main import db

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@general_bp.route('/')
def home():
    all_data = Users.query.all()
	return render_template('general/content.html', employees=all_data)

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
    name = request.form['name']
    age = request.form['age']
    my_data = User(name=name, age=age)
    db.session.add(my_data)
    db.session.commit()
    pesan = u'Data is posted to MySQL!'
    flash(pesan, 'success')
	return redirect(url_for('home'))

@general_bp.route('/edit', methods=['POST'])
def edit():
    my_data = User.query.get(result.id_user)
    my_data.id_data = request.form['id']
    my_data.title = request.form['title']
    my_data.body = request.form['body']
    db.session.commit()
    pesan = u'Data i is updated on MySQL!'
    flash(pesan, 'success')
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
    my_data = User.query.get(id_data)
    db.session.delete(my_data)
    db.session.commit()
    pesan = u'Data i is deleted on MySQL!'
    flash(pesan, 'success')
	return redirect(url_for('home'))

# @general_bp.route("/delete", methods=["POST"])
# def delete():
#     title = request.form.get("title")
#     book = Book.query.filter_by(title=title).first()
#     db.session.delete(book)
#     db.session.commit()
#     return redirect("/")