from flask import json, jsonify, request
from flask_app import app
from flask_app.models.todos_model import Todo

@app.route( "/api/todos", methods=["GET"] )
def api_get_all():
    list_todos = Todo.api_get_all()
    return ( jsonify( list_todos ) , 200 )

@app.route( "/api/new/todo", methods=["POST"] )
def api_add_one():
    new_todo = json.loads( request.data.decode( "UTF-8" ) )
    todo_id = Todo.create_one( new_todo )
    response = {
        "message" : "Successfully added the TODO!",
        "todo_id" : todo_id
    }
    return ( response, 201 )

@app.route( "/api/delete/todo/<int:id>", methods=["DELETE"] )
def api_delete_one( id ):
    data = {
        "todo_id" : id
    }
    Todo.delete_one( data )
    return ( jsonify({}), 204 )

@app.route( "/api/update/todo/<int:id>", methods=["PUT"] )
def api_update_one( id ):
    update_todo = json.loads( request.data.decode( "UTF-8" ) )
    update_todo["todo_id"] = id
    Todo.update_one( update_todo )
    response = {
        "message" : "Successfully udated the TODO!",
        "todo_id" : id
    }
    return ( jsonify( response ), 202 )
