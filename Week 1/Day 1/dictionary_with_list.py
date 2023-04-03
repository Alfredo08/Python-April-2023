student = {
    "first_name" : ["Alex", "Martha", "Roger"],
    "last_name" : ["Miller", "Smith", "Anderson"],
    "age" : [20, 25, 28],
    "stacks" : [ "Python", "Java", "MERN" ]
}

for key in student:
    print( key, student[key] )
    for element in student[key]:
        print( element )

#for item in student["stacks"]:
#    print( item )