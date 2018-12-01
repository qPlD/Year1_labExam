# - Presentation of initial inputs:
# ie. ID + topics as list.

Dev1 = [123,'Topic1','Topic2','Topic3','Topic6']

Dev2 = [456,'Topic1','Topic2','Topic4']

match = [Dev2[0]]

# Device 1 is set to be the searching device

# The ID of Device 2 is stored by default when pairing

for topicA in range(1,len(Dev1)):
    
    for topicB in range(1,len(Dev2)):
        
        if Dev1[topicA]== Dev2[topicB]:

            # Search for matching topics
            
            match = match + [Dev1[topicA]]
            
if len(match)>=2:
    
    print 'A user with',len(match)-1, 'matching interests has been found !'
    
    print '\nUser ID:',match[0],'- Common interests:',match[1:len(match)]
    
else:
    
    match = []
    
    # Adress of 2nd device is cleared if no interests have been found.






