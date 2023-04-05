from classes_pkg.animal import Animal

class Dog( Animal ):
    def __init__( self, name, owner, breed, color ):
        super().__init__( name, owner )
        self.breed = breed
        self.color = color
    
    def print_dog_info( self ):
        super().print_info()
        print( f"Dog breed: {self.breed} Dog color: {self.color}" )
    # Overriding
    def print_info( self ):
        super().print_info()
        print( f"Dog breed: {self.breed} Dog color: {self.color}" )
    # Polymorphism
    def walk_animal( self ):
        print( "I am a dog so I need to be walked twice a day!" )
