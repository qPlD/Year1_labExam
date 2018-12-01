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
userData = [
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
# Add your code from here


