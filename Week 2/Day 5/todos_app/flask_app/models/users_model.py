from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX
from flask_app.models import todos_model
from flask import flash

class User:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.list_of_todos = []
    
    @classmethod
    def get_one_with_todos( cls, data ):
        query  = "SELECT * "
        query += "FROM users u LEFT JOIN todos t "
        query += "ON u.id = t.user_id "
        query += "WHERE u.id = %(user_id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_user = cls( result[0] )

        for row in result:
            if row['t.id'] != None:
                current_todo = {
                    "id" : row['t.id'],
                    "name" : row['name'],
                    "status" : row['status'],
                    "user_id" : row['user_id'],
                    "created_at" : row['t.created_at'],
                    "updated_at" : row['t.updated_at']
                }
                current_user.list_of_todos.append( todos_model.Todo(current_todo) )
        return current_user
    
    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO users( first_name, last_name, email, password ) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result

    @staticmethod
    def validate_user( new_user ):
        is_valid = True

        if len( new_user['first_name'] ) < 3:
            flash( "You must provide your first name. At least 3 letters.", "error_first_name" )
            is_valid = False
        if len( new_user['last_name'] ) < 3:
            flash( "You must provide your last name. At least 3 letters.", "error_last_name" )
            is_valid = False
        if len( new_user['password'] ) <= 5:
            flash( "Your password must at least have 5 letters.", "error_password" )
            is_valid = False
        if new_user['password'] != new_user['password_confirmation']:
            flash( "Your passwords do not match.", "error_password" )
            is_valid = False
        if not EMAIL_REGEX.match( new_user['email'] ):
            flash( "Please provide a valid email address.", "error_email" )
            is_valid = False
        
        return is_valid


