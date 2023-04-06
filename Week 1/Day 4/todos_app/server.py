from flask import Flask, render_template

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
def display_todos():
    first_name = "Alex"
    last_name = "Miller"
    return render_template( "index.html", first_name = first_name, last_name = last_name, list_of_todos = list_of_todos )


@app.route( "/home", methods=["GET"] )
def hello_class():
    return "Hey there class of Python/Flask April 2023!"

@app.route( "/info", methods=["GET"] )
def hello_class_with_info():
    message = "I hope you enjoy working with Flask."
    return f"Hey class {message}"

@app.route( "/hello/<string:first_name>/<string:last_name>", methods=["GET"] )
def greet_someone( first_name, last_name ):
    print( f"Hey there {first_name} {last_name}" )
    return f"<h1> Welcome back {first_name} {last_name} </h1>"

@app.route( "/students", methods=["GET"] )
def display_list_of_students():
    student_list = [ "Alex", "Martha", "Roger", "Julie" ]
    result = ""

    for student in student_list:
        result += f"<p> {student} </p>"
    return f"<h1> The students of this class </h1> {result}"


if __name__ == "__main__":
    app.run( debug = True, port = 5001 )
