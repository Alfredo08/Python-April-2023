students = [ "Alex", "Martha", "Roger", "Julie" ]

# for( let i = 0; i < students.length; i++ )
for i in range( len( students ) ):
    print( students[i] )

for i in range( 5 ): # i < 5
    print( i )
print( "-----" ) 
for i in range( 2, 5 ): # i = 2   i < 5
    print( i )
print( "-----" )
            # Starting point of i, stopping point i < 20,  increment/decrement of the i
for i in range( 2, 20, 3 ): # i = 2   i < 20   i += 3
    print( i )
print( "-----" )
                # Starting point of i, stopping point i > -1,  increment/decrement of the i
for i in range( len( students ) - 1 , -1, -1 ):
    print( students[i] )
print( "-----" )
index = 0
for name in students:
    print( name )
    print( index )
    index += 1
print( "-----" )

student_info = {
    "first_name" : "Alex",
    "last_name" : "Miller",
    "age" : 20,
    "stacks" : [ "Python", "Java", "MERN" ]
}

for key in student_info:
    print( key, student_info[ key ] )

