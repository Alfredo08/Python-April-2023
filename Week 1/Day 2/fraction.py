
class Fraction:
    # Constructor
    def __init__( self, numerator, denominator ):
        # Attributes
        self.numerator = numerator
        self.denominator = denominator
    
    # Instance methods
    def print_info( self ):
        print( f"{self.numerator}/{self.denominator}" )

    def add_one_half( self ):
        result_num = ( self.numerator * 2 + self.denominator * 1 )
        result_den = ( self.denominator * 2 )
        new_fraction = Fraction( result_num, result_den )
        return new_fraction
    
    def add_one_half_to_current_fraction( self ):
        self.numerator = ( self.numerator * 2 + self.denominator * 1 )
        self.denominator = ( self.denominator * 2 )

    def add_fraction( self, fraction_two ):
        result_num = ( self.numerator * fraction_two.denominator + self.denominator * fraction_two.numerator )
        result_den = ( self.denominator * fraction_two.denominator )
        new_fraction = Fraction( result_num, result_den )
        return new_fraction


fraction_one = Fraction( 4, 9 )
fraction_two = Fraction( 1, 3 )

total = fraction_one.add_fraction( fraction_two )
total.print_info()

total2 = fraction_two.add_fraction( fraction_one )
total.print_info()

#total = fraction_one.add_one_half()
#total.print_info()
#fraction_one.print_info()
#print( "------" )
#fraction_two.print_info()
#fraction_two.add_one_half_to_current_fraction()
#fraction_two.print_info()

