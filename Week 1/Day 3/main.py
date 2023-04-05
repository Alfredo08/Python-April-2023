from classes_pkg.animal import Animal
from classes_pkg.dog import Dog
from classes_pkg.cat import Cat

list_of_dogs = []
print( "***** MENU OF OPTIONS ***** " )
print( "1) Add a dog to the list" )
print( "2) Display all dogs" )
print( "5) Terminate this program" )

option = input( "Please select an option: " )

while option != "5":
    if option == "1":
        dog_name = input( "Please type the name of the dog: " )
        dog_owner = input( f"Who is the owner of {dog_name}: " )
        dog_breed = input( f"Please type the dog breed of {dog_name}: " )
        dog_color = input( f"Please type the color of {dog_name}: " )
        new_dog = Dog( dog_name, dog_owner, dog_breed, dog_color )
        list_of_dogs.append( new_dog )
    if option == "2":
        for dog in list_of_dogs:
            dog.print_info()
    
    print( "***** MENU OF OPTIONS ***** " )
    print( "1) Add a dog to the list" )
    print( "2) Display all dogs" )
    print( "5) Terminate this program" )

    option = input( "Please select an option: " )


# message = input( "Please leave a comment: " )
# print( f"Your message is: {message}" )

# pet_one = Animal( "Rocky", "Alex" )
# pet_two = Animal( "Max", "Martha" )
# dog_jagger = Dog( "Jagger", "Alfredo", "Golden Retriever", "Golden" )
# cat_chester = Cat( "Chester", "Alfredo", "Small" )


# dog_jagger.print_info()

# dog_jagger.walk_animal()
# cat_chester.walk_animal()
# cat_chester.print_info()