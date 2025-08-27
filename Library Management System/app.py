from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO books(title, author, genre) VALUES(%s,%s,%s)", (title, author, genre))
        mysql.connection.commit()
        cur.close()
        flash("Book added successfully!", "success")
        return redirect(url_for('view_books'))
    return render_template('add_book.html')

@app.route('/view_books')
def view_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return render_template('view_books.html', books=books)

@app.route('/api/books')
def api_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    books_list = [{"id": b[0], "title": b[1], "author": b[2], "genre": b[3], "available": bool(b[4])} for b in books]
    return jsonify(books_list)

if __name__ == '__main__':
    app.run(debug=True)
