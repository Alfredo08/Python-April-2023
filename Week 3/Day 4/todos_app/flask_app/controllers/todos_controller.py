from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.todos_model import Todo

@app.route( "/todos", methods=["GET"] )
def get_todos():
    if "user_id" not in session:
        return redirect( "/" )
    list_of_todos = Todo.get_all()
    return render_template( "todos.html", list_of_todos = list_of_todos )

@app.route( "/todo/form", methods=["GET"] )
def display_todo_form():
    if "user_id" not in session:
        return redirect( "/" )
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
    if "user_id" not in session:
        return redirect( "/" )
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

@app.route( "/todo/<int:id>", methods=['GET'] )
def get_one_todo( id ):
    if "user_id" not in session:
        return redirect( "/" )
    data = {
        "todo_id" : id
    }
    current_todo = Todo.get_one( data )
    return render_template( "todo.html", current_todo = current_todo )