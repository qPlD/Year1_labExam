'''

y = [4]*3
print y

li = []
inp = raw_input( "type a word then Enter ('end' to finish: " )
while inp != "end":
    li = li + [ inp ]
    inp = raw_input( "next word, please: " )
print li




longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17,
             19, 20, 21, 22, 23, 24, 25, 26, 31,
             32, 33, 34, 35, 37, 40, 43, 45, 48,
             50, 51, 53, 55, 56, 57, 58, 59, 60,
             61, 62, 63, 64, 66, 69, 72, 73, 74,
             75, 77, 78, 79, 80, 81, 82, 83, 85,
             86, 87, 88, 89, 92, 93, 94, 95, 97, 99, 100 ]
shortList = [ 5, 9, 14, 55, 67, 94 ]
# creates two lists of different lengths
# Count the number of items that appear in both shortList and longList
count = 0 # is set to 0
for shortListItem in shortList: # for each item of the small list
    for longListItem in longList: # the prog will look at all the items of the long list
        if shortListItem == longListItem: # if some items are matching
            count = count + 1 # the count variable is incremented by 1

print "The number of matches is", count # outputs the amount of matches between the lists



longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17 ]
shortList = [ 5, 12, 17 ]

# shortList is a subset of longList - all shortList items are in longList
# identify the difference between the two lists - items in longList that aren't in shortList

differenceList = [] # creates an empty list to store all the different values
for longListItem in longList: # for each item in the big list
    if longListItem not in shortList: # which isnt in the short list
            differenceList = differenceList + [ longListItem ] # the item is added to the empty list

print "The difference list is", differenceList # prints all the items in longlist but not in shortlist



import random
# random package to use random function
# Create a list of random numbers
numbersList = [] # list in initially empty
listLen = 100
for i in range( listLen ): # will execute 99 times
    numbersList = numbersList + [ random.randint( 0, 100 ) ]# adds a random number to the list

# Find the largest value in the list
largest = 0

for index in range( 1, listLen ):#will run 99 times
    if numbersList[ index ] > numbersList[ largest ]: #if the number at pos 1> than number at pos 0
        largest = index #largest moves to 1, and index will move to 2
# each value is compared to the previous greatest one to see if it is bigger
print "The list is:"
print numbersList
print "The largest item in the list is at position:", largest



import random
# imports package
longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17 ]

# Pick 2 unique numbers from longList, at random - any 2 numbers as long
# as they're not the same

uniques = [ longList[ random.randint( 0, len( longList ) - 1 ) ] ]
#takes a random value in the list at index 0 to n-1 (index of last value)
while len( uniques ) < 2:#while the list has less than 2 values
    nextCandidate = random.randint( 0, len( longList ) - 1 )# finds a new random index (which holds a value)
    if longList[ nextCandidate ] != uniques[ 0 ]: #if it has not already been chosen
        uniques = uniques + [ longList[ nextCandidate ] ] # it is added to the list

print longList
print "The unique numbers are", uniques[ 0 ], "and", uniques[ 1 ]
# prints 2 uniques numbers chosen randomly from that list.



import random

# Create a list of random numbers
numbersList = [] # creates an empty list
listLen = 100
for i in range( listLen ): # will run 99 times
    numbersList = numbersList + [ random.randint( 0, 100 ) ] # adds a random number to the list
# the list now has 99 entries of numbers between 0 and 99
# Search for a number in the list
print numbersList
searchValue = input( "Enter the number to search for: " )

found = False 
index = 0

while not found and index < listLen: #while these variables are smaller than 100
# if found is true, it breaks the while loop
    if searchValue == numbersList[ index ]: #if the number searched for is in the list.
        found = True #boolean set to true
    else:
        index = index + 1 #index is incremented

print "The list is:"
print numbersList
if found:
   print searchValue, "found at position", index
else:
    print "The value", searchValue, "is not in the list"
    # this only prints the first value, not the others if there are more.

'''

import random

# A list of book titles
books = [ \
    "Birdsong", \
    "Master and Commander", \
    "Chocolat", \
    "The Remains of the Day", \
    "The Shipping News", \
    "Nice work", \
    "Monsignor Quixote", \
    "Childhood's End", \
    "A Town Like Alice", \
    "Doctor Zhivago", \
    "1984", \
    "Tess of the D'Urbervilles", \
    "The Cider House Rules", \
    "The Grapes of Wrath", \
    "Man's Search for Meaning", \
    "The Paradox of Choice", \
    "The Name of the Rose", \
    "Death and the Penguin", \
    "The Inheritors", \
    "Riotous Assembly", \
    "The Subtle Knife", \
    "Brave New World", \
    "The Philosopher's Stone", \
    "To the Lighthouse", \
    "The War of the Worlds", \
    "The Kraken Wakes", \
    "About a Boy", \
    "Love in the Time of Cholera", \
]

# Each entry in this list is a list of purchases for a single user.
# The numbers used in the list are indexes into the list above.
# Hence, 4 in the first list below indicates that this user purchased
# the book with title at index 4 of the list above - i.e. The Shipping News.
userData = [ #this is a list of other lists, each sublist is the purchases of a single user.
    [ 4, 6, 9, 11, 14, 16, 19, 20, 21, 22, 26 ],
    [ 2, 3, 7, 8, 10, 12, 13, 15, 16, 17, 18, 19, 21, 23, 24, 25, 26 ],
    [ 1, 2, 7, 8, 12, 13, 17, 18, 21, 23, 25 ],
    [ 0, 1, 3, 5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 21, 25, 26, 27 ],
    [ 6, 27 ],
    [ 0, 1, 3, 4, 7, 8, 9, 11, 12, 13, 15, 16, 18, 22, 25 ],
    [ 4, 9, 10, 15, 16, 19, 23, 24, 26 ],
    [ 0, 1, 4, 13, 17, 20, 22, 24, 25 ],
    [ 5, 14 ],
    [ 5, 6, 8, 10, 17, 18, 19, 21, 22, 24, 26, 27 ],
    [ 0, 3, 5, 7, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 26 ],
    [ 2, 3, 11, 21, 24 ],
    [ 7 ],
    [ 0, 1, 4, 6, 9, 10, 13, 18, 22, 26 ],
    [ 1, 2, 5, 6, 8, 9, 10, 12, 14, 15, 17, 18, 23, 27 ],
    [ 4, 13, 16, 25 ],
    [ 5, 6, 8, 10, 11, 12, 13, 14, 16, 17, 18, 21, 26 ],
    [ 0, 13, 17, 18, 21 ],
    [ 0, 3, 5, 10, 15, 16, 20, 21, 22, 23, 25, 26 ],
    [ 0, 1, 3, 4, 5, 6, 8, 10, 11, 12, 15, 16, 17, 18, 22, 24, 25, 27 ],
    [ 0, 1, 4, 5, 6, 8, 9, 10, 11, 12, 20, 21, 22, 23, 24, 25, 27 ],
    [ 1, 5, 6, 9, 12, 14, 15, 16, 17, 21, 22, 24, 25, 27 ],
    [ 14, 18 ],
    [ 3, 5, 16, 20, 22, 23, 26, 27 ],
    [ 1, 3, 4, 5, 6, 11, 12, 14, 15, 17, 18, 20, 25, 26, 27 ],
    [ 0, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 23, 24, 25, 27 ],
    [ 5, 22 ],
    [ 1, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 21, 22, 23, 24, 25 ],
    [ 0, 1, 5, 11, 12, 16, 17, 21, 22 ],
    [ 0, 1, 3, 5, 6, 7, 9, 10, 11, 12, 14, 20, 21, 24, 25, 27 ]
]

#----------------------------------------
#a)
userPurch = []
purch = 0
while purch < 28:
    purch = input('\nWhat book (IDs) have you bought so far? \nType an integer >27 to signal you have entered all IDs: ')
    if purch < 28:
        userPurch = userPurch + [purch]
print '\nYour purchased books are',userPurch

#b)
count = 0
t = 0
n = len(userData)
matches = []
while t < n:
    #print userData[t]
    for itemuP in userPurch:
        for itemuD in userData[t]:
            if itemuP == itemuD:
                count = count + 1
    matches = matches + [count]
    count = 0
    t = t + 1

print '\nAmount of similarities with each other user: \n',matches

#c)
largest = 0
samevalues= []
for i in range(1,len(matches)):
    
    if matches[i] > matches[largest]:
        largest = i
        
    elif matches[i] == matches[largest] and i<len(matches):
        samevalues= samevalues + [i]
        
del samevalues [0]

if samevalues != [] and matches[samevalues[0]]==matches[largest]:
    samevalues = samevalues + [largest]
    print '\nUsers with whom you have same biggest amount of matches: \n',samevalues
    largest = samevalues[random.randint(0,len(samevalues)-1)]
    print '\nRandomly selected user between those biggest amount: \n',largest

#d)
candidates = []
for w in userData[largest]:
    if w not in userPurch:
        candidates = candidates + [w]
print '\nThe different purchases between you and user',largest,'is: \n', candidates

#e)
recom = [candidates[random.randint(0,len(candidates)-1)]]

while len(recom) < 4:
    nextCandidate = random.randint(0,len(candidates)-1)
    if candidates[nextCandidate] not in recom:
        recom = recom + [candidates[nextCandidate]]

print "\nThe 4 random recommandations are: \n", recom

#f)
recombooks = [books[recom[0]],books[recom[1]],books[recom[2]],books[recom[3]]]
g=0
for q in recombooks:
    g=0
    while g<len(books):
        if q == books[g]:
            del books[g]
        g=g+1
print '\nBooks you have not read are:',books
print '\nYet, we suggest you read:', recombooks
