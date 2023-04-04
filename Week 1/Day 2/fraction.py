
class Fraction:
    list_of_fractions = []
    description = "Class to represent a fraction"
    # Constructor
    def __init__( self, numerator, denominator ):
        # Attributes
        self.numerator = numerator
        self.denominator = denominator
        Fraction.list_of_fractions.append( self )
    
    # Instance methods
    def print_info( self ):
        print( f"{self.numerator}/{self.denominator}" )
        return self

    def add_one_half( self ):
        result_num = ( self.numerator * 2 + self.denominator * 1 )
        result_den = ( self.denominator * 2 )
        new_fraction = Fraction( result_num, result_den )
        return new_fraction
    
    def add_one_half_to_current_fraction( self ):
        self.numerator = ( self.numerator * 2 + self.denominator * 1 )
        self.denominator = ( self.denominator * 2 )
        return self

    def add_fraction( self, fraction_two ):
        result_num = ( self.numerator * fraction_two.denominator + self.denominator * fraction_two.numerator )
        result_den = ( self.denominator * fraction_two.denominator )
        new_fraction = Fraction( result_num, result_den )
        return new_fraction
    
    @classmethod
    def print_all_fractions( cls ):
        for fraction in cls.list_of_fractions:
            fraction.print_info()

    @staticmethod
    def add_two_numbers( num1, num2 ):
        return num1 + num2
    

fraction_one = Fraction( 4, 9 )
fraction_two = Fraction( 1, 3 )
fraction_three = Fraction( 2, 4 ) 

fraction_one.add_one_half_to_current_fraction().print_info()
fraction_one.add_fraction( fraction_two )

#print( fraction_one.description )
#print( fraction_two.description )
#print( fraction_three.description )

#fraction_two.description = "This will change just for fraction 2"

#Fraction.description = "Learning about class methods right now"

#print( fraction_one.description )
#print( fraction_two.description )
#print( fraction_three.description )
#total = fraction_one.add_fraction( fraction_two )
#total.print_info()

#total2 = fraction_two.add_fraction( fraction_one )
#total.print_info()

#total = fraction_one.add_one_half()
#total.print_info()
#fraction_one.print_info()
##print( "------" )
#fraction_two.print_info()
#fraction_two.add_one_half_to_current_fraction()
#fraction_two.print_info()

#Fraction.print_all_fractions()

#print( Fraction.add_two_numbers( 50, 100 ) )

