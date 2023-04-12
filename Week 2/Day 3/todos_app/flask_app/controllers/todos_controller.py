from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.todos_model import Todo

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

@app.route( "/todo/delete/<int:id>", methods=['POST'] )
def delete_todo( id ):
    data = {
        "todo_id" : id
    }
    Todo.delete_one( data )
    return redirect( '/todos' )

@app.route( "/todo/edit/form/<int:id>", methods=['GET'] )
def display_todo_edit_form( id ):
    data = {
        "todo_id" : id
    }
    current_todo = Todo.get_one( data )
    return render_template( "todo_edit_form.html", current_todo = current_todo )

@app.route( "/todo/update/<int:id>", methods=['POST'] )
def update_todo( id ):
    update_todo = {
        "name" : request.form["todo_name"],
        "status" : request.form["todo_status"],
        "user_id" : session["user_id"],
        "todo_id" : id
    }
    Todo.update_one( update_todo )
    return redirect( "/todos" )