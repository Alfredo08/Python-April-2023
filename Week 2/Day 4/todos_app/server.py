from flask_app import app
from flask_app.controllers import todos_controller, users_controller

if __name__ == "__main__":
    app.run( debug = True, port = 5001 )


"""
Method: GET
Grabbing everything of a list
URL: "/todos"
Function: get_all_todos()
          get_todos()

Method: GET
Grabbing one of a particular list
URL: "/todo/<int:id>"
     "/user/<int:id>"
Function: get_todo_by_id( id )
          get_todo( id )

Method: GET
Displaying a form that will eventually refer to a list
URL: "/todo/form"
Function: display_todo_form()

Method: POST
Create a new item of a list
URL: "/todo/add"
     "/todo/new"
Function: create_todo()
          add_todo()
          new_todo()

Method: POST - PUT
Updating an existing item of a list
URL: "/todo/update/<int:id>"
     "/todo/edit/<int:id>"
Function: update_todo( id )
          edit_todo( id )

Method: POST - DELETE
Deleting an existing item of a list
URL: "/todo/remove/<int:id>"
     "/todo/delete/<int:id>"
Function: remove_todo( id )
          delete_todo( id )
"""