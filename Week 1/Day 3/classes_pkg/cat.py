from classes_pkg.animal import Animal

class Cat( Animal ):
    def __init__( self, name, owner, size ):
        super().__init__( name, owner )
        self.size = size
    
    # Polymorphism
    def walk_animal( self ):
        print( "I don't need to be walked human!" )