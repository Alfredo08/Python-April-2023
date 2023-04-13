from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.users_model import User

@app.route( "/todos/user", methods = ['GET'] )
def get_user_with_todos():
    data = {
        "user_id" : session['user_id']
    }
    current_user = User.get_one_with_todos( data )
    return render_template( "user_with_todos.html", current_user = current_user )
