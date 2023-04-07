from flask import Flask, render_template, redirect, request

app = Flask( __name__ )

list_of_todos = [
    {
        "id" : 123,
        "name" : "Learning flask",
        "status" : "in_progress"
    },
    {
        "id" : 456,
        "name" : "Learning routes",
        "status" : "complete"
    },
    {
        "id" : 789,
        "name" : "Learning static content and templates",
        "status" : "in_progress"
    },
    {
        "id" : 555,
        "name" : "Learning POST",
        "status" : "pending"
    }
]

@app.route( "/todos", methods=["GET"] )
def get_todos():
    first_name = "Alex"
    last_name = "Miller"
    return render_template( "todos.html", first_name = first_name, last_name = last_name, list_of_todos = list_of_todos )

@app.route( "/todo/form", methods=["GET"] )
def display_todo_form():
    return render_template( "todo_form.html" )

@app.route( "/todo/new", methods=["POST"] )
def create_todo():
    print( request.form )
    new_todo = {
        "id" : request.form["todo_id"],
        "name" : request.form["todo_name"],
        "status" : request.form["todo_status"]
    }
    list_of_todos.append( new_todo )
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