from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import todos_model

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

