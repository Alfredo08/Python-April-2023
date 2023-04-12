from mysqlconnection import connectToMySQL

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

        result = connectToMySQL( "todos_db" ).query_db( query )

        list_of_todos = []
        for row in result:
            list_of_todos.append( cls( row ) )
            # list_of_todos.append( Todo( row ) )
        return list_of_todos

    @classmethod
    def create_one( cls, data ):
        query  = "INSERT INTO todos( name, status, user_id ) "
        query += "VALUES ( %(name)s, %(status)s, %(user_id)s ); "

        result = connectToMySQL( "todos_db" ).query_db( query, data )
        return result
    
