
def add_nums_in_list( list_numbers ):
    total = 0
    for i in range( len( list_numbers ) ):
        total += list_numbers[i]
    return total

data = [ 1, 2, 3, 4, 5 ]

print( add_nums_in_list( data ) )