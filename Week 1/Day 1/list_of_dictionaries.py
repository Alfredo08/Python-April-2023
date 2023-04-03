users = [
    {
        "first": "Ada", 
        "last": "Lovelace"
    }, # index 0
    {
        "first": "Alan", 
        "last": "Turing"
    }, # index 1
    {
        "first": "Eric", 
        "last": "Idle"
    } # index 2
]

for i in range( len( users ) ):
    # print( users[i]["first"], users[i]["last"], i )
    for key in users[i]:
        print( key, users[i][key] )