from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users_model

class Todo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.status = data['status']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod
    def get_all( cls ):
        query  = "SELECT * "
        query += "FROM todos;"

        result = connectToMySQL( DATABASE ).query_db( query )

        list_of_todos = []
        for row in result:
            list_of_todos.append( cls( row ) )
            # list_of_todos.append( Todo( row ) )
        return list_of_todos
    
    @classmethod
    def api_get_all( cls ):
        query  = "SELECT * "
        query += "FROM todos;"
        return connectToMySQL( DATABASE ).query_db( query )

    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO todos( name, status, user_id ) "
        query += "VALUES ( %(name)s, %(status)s, %(user_id)s ); "

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    @classmethod
    def delete_one( cls, data ):
        query  = "DELETE FROM todos "
        query += "WHERE id = %(todo_id)s;"
        # Deleting something from the Database doesn't returns anything: None
        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result

    @classmethod
    def get_one( cls, data ):
        query  = "SELECT * "
        query += "FROM todos "
        query += "WHERE id = %(todo_id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        current_todo = cls( result[0] )
        return current_todo
    
    @classmethod
    def update_one( cls, data ):
        query  = "UPDATE todos "
        query += "SET name = %(name)s, status = %(status)s, user_id = %(user_id)s "
        query += "WHERE id = %(todo_id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        return result
    
    @classmethod
    def get_one( cls, data ):
        query  = "SELECT * "
        query += "FROM todos t JOIN users u "
        query += "ON t.user_id = u.id "
        query += "WHERE t.id = %(todo_id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )
        row = result[0]
        current_todo = cls( row )
        current_user = {
            "id" : row['u.id'],
            "first_name" : row['first_name'],
            "last_name" : row['last_name'],
            "email" : row['email'],
            "password" : row['password'],
            "updated_at" : row['u.updated_at'],
            "created_at" : row['u.created_at']
        }
        current_todo.user = users_model.User( current_user )
        return current_todo
