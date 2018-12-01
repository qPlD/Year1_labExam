'''
#v
s = raw_input('Enter text:')
i = len(s)-1
while i >= 0:
    print s[i]
    i = i - 1

#vi
s = raw_input('Enter text:')
i = 1
while i < len(s):
    if i%2==0:
        print s[i]
    i = i + 1

#vii
s = raw_input('Enter text:')
i = len(s)-1
w = 0
while w < len(s) and i >=  0:
    print s[w],s[i]
    i = i - 1
    w = w + 1

#2
s = raw_input('Enter text:')
i = len(s)-1
w = 0
palind = 0
while w < len(s) and i >=  0:
    print s[w],s[i]
    if s[w]==s[i]:
        palind = palind + 1
    i = i - 1
    w = w + 1
if palind == len(s):
    print s, 'is a palindrome'

#second option for doing it
s = raw_input('Enter text:')
i = len(s)-1
w = 0
palind = 1 #1 stands for true
while w < len(s) and i >=  0:
    print s[w],s[i]
    if s[w]!=s[i]:
        palind = 0 #0 stands for false
    i = i - 1
    w = w + 1
if palind == 1:
    print s, 'is a palindrome'

'''
#3
import string
s = raw_input('Enter a full phrase:')
punctuation = '!:/;.,?'
for char in s:
    if char not in punctuation:
        print char,
    
    
