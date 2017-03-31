from flask import Flask, render_template, request, redirect, url_for

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'bookkart'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# @ signifies a detector - way to wrap a function and modifying its behavior
@app.route('/')
def  index():
	return render_template("index.html")

@app.route("/searching", methods=['POST','GET'])
def searching():
	_search_by = request.form['searchby']
	_book_or_genre = request.form['bookorgenre']
	
	try:
		db = mysql.connect()
		curr = db.cursor()
		if _search_by.lower() == "book":
			curr.execute("SELECT * from book_details where book_name = '"+_book_or_genre+"';")
		elif _search_by.lower() == "genre":
			curr.execute("SELECT * from book_details where genre = '"+_book_or_genre+"';")
		else:
			return redirect(url_for('index'))

		data = curr.fetchone()
		curr.nextset()
		data_array = []
		while not data is None:
			data_array.append(data)
			data = curr.fetchone()
			curr.nextset()
		return render_template("search_result.html", data_array = data_array)
	
	except Exception as e:
		return str(e)

@app.route("/add_success", methods=['POST','GET'])
def add_success():
	_b_name = request.form['inputBookName']
	_b_author = request.form['inputAuthor']
	_b_genre = request.form['inputGenre']
	_b_copies = int(request.form['inputCopies'])

	try:
		db = mysql.connect()
		curr = db.cursor()
		curr.callproc("new_book",(_b_name, _b_author, _b_genre, _b_copies))
		check = curr.fetchall();
		if len(check) is 0:
			db.commit()
		data_array = [_b_name, _b_author, _b_genre, _b_copies]
		return render_template("add_success.html", data_array = data_array)
	except Exception as e:
		return str(e)


@app.route('/showSignUp')
def showSignUp():
	return render_template("SignUp.html")

@app.route('/showSignIn')
def showSignIn():
	return render_template("SignIn.html")

@app.route('/add_book')
def add_book():
	return render_template("AddBook.html")

@app.route('/success')
def success():
	return render_template("Success.html")

if __name__ == "__main__":
	app.run(debug=True)