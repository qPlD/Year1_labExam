import random

# Create a list of random numbers
numbersList = []
listLen = 100
for i in range( listLen ):
    numbersList = numbersList + [ random.randint( 0, 100 ) ]

# Find the largest value in the list
largest = 0

for index in range( 1, listLen ):
    if numbersList[ index ] > numbersList[ largest ]:
        largest = index

print "The list is:"
print numbersList
print "The largest item in the list is at position:", largest
    
