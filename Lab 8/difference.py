

longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17 ]
shortList = [ 5, 12, 17 ]

# shortList is a subset of longList - all shortList items are in longList
# identify the difference between the two lists - items in longList that aren't in shortList

differenceList = []
for longListItem in longList:
    if longListItem not in shortList:
            differenceList = differenceList + [ longListItem ]

print "The difference list is", differenceList
