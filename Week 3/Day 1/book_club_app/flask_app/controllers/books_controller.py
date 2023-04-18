from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.book_model import Book

@app.route( "/books", methods=["GET"] )
def get_books():
    all_books = Book.get_all_with_users()
    return render_template( "books.html", all_books = all_books )

@app.route( "/book/form", methods=["GET"] )
def display_book_form():
    return render_template( "book_form.html" )

@app.route( "/book/new", methods=["POST"] )
def add_book():
    data = {
        **request.form,
        "user_id" : session["user_id"]
    }
    if Book.validate_book( data ) == False:
        return redirect( "/book/form" )
    Book.create_one( data )
    return redirect( "/books" )