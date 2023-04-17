from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User

@app.route( "/", methods=["GET"] )
def display_login_registration():
    return render_template( "index.html" )

@app.route( "/user/new", methods=["POST"] )
def create_user():
    if User.validate_user( request.form ) == False:
        return redirect( "/" )
    encrypted_password = User.encrypt_string( request.form["password"] )
    data = {
        **request.form,
        "password" : encrypted_password
    }
    user_id = User.create_one( data )
    session["user_id"] = user_id
    return redirect( "/" )