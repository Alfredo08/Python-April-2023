from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.users_model import User

@app.route( "/todos/user", methods = ['GET'] )
def get_user_with_todos():
    if "user_id" not in session:
        return redirect( "/" )
    data = {
        "user_id" : session['user_id']
    }
    current_user = User.get_one_with_todos( data )
    return render_template( "user_with_todos.html", current_user = current_user )

@app.route( "/", methods = ["GET"] )
@app.route( "/registration", methods = ["GET"] )
@app.route( "/login", methods = ["GET"] )
def display_login_registration():
    return render_template( "index.html" )

@app.route( "/user/new", methods = ['POST'] )
def create_user():
    new_user = {
        **request.form
    }

    if User.validate_user( new_user ) == False:
        return redirect( "/" )
    else:
        new_user["password"] = User.encrypt_string( new_user['password'] )
        user_id = User.create_one( new_user )
        session['user_id'] = user_id
        session['full_name'] = new_user['first_name'] + " " + new_user['last_name']
        return redirect( "/todos" )
    
@app.route( "/login", methods = ['POST'] )
def process_login():
    data = {
        "email" : request.form['email']
    }
    current_user = User.get_one_by_email( data )
    if current_user == None:
        return redirect( "/" )
    else:
        if User.validate_password( request.form['password'], current_user.password ) == False:
            return redirect( "/" )
        else:
            session['user_id'] = current_user.id
            session['full_name'] = current_user.first_name + " " + current_user.last_name
            return redirect( "/todos" )
        
@app.route( "/logout", methods = ['POST'] )
def process_logout():
    session.clear()
    # del session["user_id"]
    # del session["full_name"]
    return redirect( "/" )