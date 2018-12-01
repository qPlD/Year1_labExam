from string import *

# Program to index sentences

# Author:   <***MUST DO*** - REPLACE THIS WITH YOUR NAME AND STUDENT ID>

# Date:


def RemovePunct(line):
    newline = ''
    
    for letter in line:
        PUNCT = False
        for char in punctuation:
            if letter == char:
                PUNCT = True
                

        if PUNCT == False:
            newline = newline + letter

    return newline

def RemoveSW(line):
    line = str.split(line)
    newline = []
    
    for value in line:
        StopW = False
        for element in stopWords:
            if value == element:
                StopW = True
                
        if StopW == False:
            newline = newline + [value]

    return newline
                


def StemWord(line):
    newline = []
    
    for word in line:
        for stems in Stem:
            if word not in noStemWords and word[-len(stems):] == stems:
                word = word[:len(word)-len(stems)]
                
                
        newline = newline + [word]

    return newline
            

           
                

stopWords = [ "a", "i", "it", "am", "at", "on", "in", "to", "too", "very", \
              "of", "from", "here", "even", "the", "but", "and", "is", "my", \
              "them", "then", "this", "that", "than", "though", "so", "are" ]

Stem = [ "s","es","ed","er","ly","ing"]

noStemWords = [ "feed", "sages", "yearling", "mass", "make", "sly", "ring" ]

punctuation = ".,:;!?&'"


Dict = {}
linecounter = 1
stoploop = False
print 'Indexer: type in lines, finish with a . at start of line only'

while stoploop == False:
    
    
    line = raw_input()
    if line == '.':
        stoploop = True
        
    line = lower(line)
    line = RemovePunct(line)
    line = RemoveSW(line)
    line = StemWord(line)
    
    
    for word in line:
        if word not in Dict:
            Dict[word] = linecounter

        elif Dict[word] != linecounter:
            Dict[word] = Dict[word], linecounter
        
        

    linecounter += 1


print 'The index is:'
punctuation = '()'
for value in Dict:
    print value, RemovePunct(str(Dict[value]))
    
'''
printed = []
linecounter = 1
while len(printed) != len(Dict):
    for key in Dict:
        if str(linecounter) in str(Dict[key]) and key not in printed:
            print key, RemovePunct(str(Dict[key]))
            printed = printed + [key]

    linecounter+=1
'''
    
    
