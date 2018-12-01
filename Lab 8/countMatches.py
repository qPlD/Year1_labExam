

longList = [ 0, 3, 4, 5, 6, 7, 8, 12, 15, 16, 17,
             19, 20, 21, 22, 23, 24, 25, 26, 31,
             32, 33, 34, 35, 37, 40, 43, 45, 48,
             50, 51, 53, 55, 56, 57, 58, 59, 60,
             61, 62, 63, 64, 66, 69, 72, 73, 74,
             75, 77, 78, 79, 80, 81, 82, 83, 85,
             86, 87, 88, 89, 92, 93, 94, 95, 97, 99, 100 ]
shortList = [ 5, 9, 14, 55, 67, 94 ]

# Count the number of items that appear in both shortList and longList
count = 0
for shortListItem in shortList:
    for longListItem in longList:
        if shortListItem == longListItem:
            count = count + 1

print "The number of matches is", count
