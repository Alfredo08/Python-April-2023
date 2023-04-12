from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Todo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.status = data['status']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
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
    
