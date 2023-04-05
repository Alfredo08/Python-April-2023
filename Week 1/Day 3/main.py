from classes_pkg.animal import Animal
from classes_pkg.dog import Dog
from classes_pkg.cat import Cat

pet_one = Animal( "Rocky", "Alex" )
pet_two = Animal( "Max", "Martha" )
dog_jagger = Dog( "Jagger", "Alfredo", "Golden Retriever", "Golden" )
cat_chester = Cat( "Chester", "Alfredo", "Small" )


dog_jagger.print_info()

dog_jagger.walk_animal()
cat_chester.walk_animal()
cat_chester.print_info()