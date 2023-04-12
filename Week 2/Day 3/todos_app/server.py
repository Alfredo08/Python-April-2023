from flask import Flask, render_template, redirect, request, session
from todos_model import Todo

app = Flask( __name__ )
app.secret_key = "password123"

@app.route( "/todos", methods=["GET"] )
def get_todos():
    session["full_name"] = "Alex Miller"
    session["user_id"] = 1
    list_of_todos = Todo.get_all()
    return render_template( "todos.html", list_of_todos = list_of_todos )

@app.route( "/todo/form", methods=["GET"] )
def display_todo_form():
    if "full_name" in session:
        session["full_name"] = "Alexander Miller"
        # print( current_user )
    else:
        print( "Be careful, session doesn't exist!" )
    return render_template( "todo_form.html")

@app.route( "/todo/new", methods=["POST"] )
def create_todo():
    print( request.form )
    new_todo = {
        "name" : request.form["todo_name"],
        "status" : request.form["todo_status"],
        "user_id" : session["user_id"]
    }
    todo_id = Todo.create_one( new_todo )
    return redirect( "/todos" )

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