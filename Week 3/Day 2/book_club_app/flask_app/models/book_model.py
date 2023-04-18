from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Book:
    def __init__( self, data ):
        self.id = data["id"]
        self.title = data["title"]
        self.author = data["author"]
        self.thoughts = data["thoughts"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None
    
    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO books( title, author, thoughts, user_id ) "
        query += "VALUES( %(title)s, %(author)s, %(thoughts)s, %(user_id)s );"
        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    @classmethod
    def get_all_with_users( cls ):
        query  = "SELECT * "
        query += "FROM books b JOIN users u "
        query += "ON b.user_id = u.id;"

        results = connectToMySQL( DATABASE ).query_db( query )
        list_of_books = []
        for row in results:
            current_book = cls( row )
            book_user = {
                "created_at" : row["u.created_at"],
                "updated_at" : row["u.updated_at"],
                "id" : row["u.id"],
                **row
            }
            current_book.user = user_model.User( book_user )
            list_of_books.append( current_book )
        return list_of_books
    
    @staticmethod
    def validate_book( data ):
        is_valid = True
        if len( data["title"] ) == 0:
            flash( "You must provide a title!.", "error_title" )
            is_valid = False
        if len( data["author"] ) == 0:
            flash( "You must provide the author!.", "error_author" )
            is_valid = False
        if len( data["thoughts"] ) == 0:
            flash( "You must provide your thoughts!.", "error_thoughts" )
            is_valid = False
        return is_valid