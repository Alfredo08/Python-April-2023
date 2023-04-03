# Leaving a comment
# JS: Numbers, Strings, Booleans, Null, Undefined
# Python: (int) whole, (float) decimal, Strings, Booleans, None
# Arrays, Dictionaries

first_name = "Alex"
age = 20
siblings = False
python_exam_score = 9.2
mern_exam_score = None

print( first_name + " " + str( age ) )
print( type( age ) )
print( type( siblings ) )
print( type( python_exam_score ) )
print( type( first_name ) )

print( first_name, age, siblings )

print( f"Hello there my name is '{first_name}' and I am {age} years old." )
print( 'Hello there my name is "%s" and I am %d years old.' % ( first_name, age ) )
print( "Hello there my name is {} and I am {} years old.".format( first_name, age ) )

print( first_name.isupper() )
print( first_name.upper() )