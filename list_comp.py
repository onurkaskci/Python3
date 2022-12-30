#CHECK FOR A LETTER IN LIST ELEMENTS AND APPEND 
random_words = ["car", "building", "computer", "banana", "notebook"]

newlist = []

for x in random_words: #loops through the random_words list as usual
    if "a" in x: #checks every list element if it has the letter a in it
        newlist.append(x) #if it does adds the current list element to the newlist

#print(newlist)

######

newlist = [x for x in random_words if "a" in x] #does all the above in one line
#print(newlist)


#REVERSE STRING LIST ELEMENTS
vehicles = ["plane", "ship", "truck", "motorbike"]
'''
reverse_vehicles = []

for x in vehicles:
    print(x[::-1])
    reverse_vehicles.append(x[::-1])

print(reverse_vehicles)
'''

#######

reverse_vehicles = [x[::-1] for x in vehicles]
print(reverse_vehicles)