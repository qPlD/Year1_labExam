import random

longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17 ]

# Pick 2 unique numbers from longList, at random - any 2 numbers as long
# as they're not the same

uniques = [ longList[ random.randint( 0, len( longList ) - 1 ) ] ]

while len( uniques ) < 2:
    nextCandidate = random.randint( 0, len( longList ) - 1 )
    if longList[ nextCandidate ] != uniques[ 0 ]:
        uniques = uniques + [ longList[ nextCandidate ] ]

print longList
print "The unique numbers are", uniques[ 0 ], "and", uniques[ 1 ]
