import random

# Create a list of random numbers
numbersList = []
listLen = 100
for i in range( listLen ):
    numbersList = numbersList + [ random.randint( 0, 100 ) ]

# Search for a number in the list
searchValue = input( "Enter the number to search for: " )

found = False
index = 0

while not found and index < listLen:
    if searchValue == numbersList[ index ]:
        found = True
    else:
        index = index + 1

print "The list is:"
print numbersList
if found:
   print searchValue, "found at position", index
else:
    print "The value", searchValue, "is not in the list"
    
