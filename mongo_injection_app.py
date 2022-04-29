from flask import Flask, request, render_template
from pymongo import MongoClient

mongoClient = MongoClient().books_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# code with NoSql-Injection vulnerability
@app.route('/books')
def books():
    isbn = request.args.get('isbn')
    query = "function(){ return this.ISBN == '%s';}" % isbn
    cursor = mongoClient.books.find({'$where': query})
    #print(list(cursor))

    return render_template('books.html', books=cursor, isbn=isbn, query=query)

# code with solution implemented
@app.route('/books_nosql_solution')
def books_nosql_solution():
    isbn = request.args.get('isbn')

    if isbn is None:
        isbn =''

    if isbn.isnumeric():
        query = "function(){ return this.ISBN == '%s';}" % isbn
        cursor = mongoClient.books.find({'$where': query})
        #   print(list(cursor))

        return render_template('books_solution.html', books=cursor, isbn=isbn, query=query, valid=True)
    else:
        cursor = []
        return render_template('books_solution.html', books=cursor, isbn=isbn, query='', valid=False)

if __name__ == '__main__':
    app.run(debug = True)
