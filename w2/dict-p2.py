# 1. Create an empty dictionary called phonebook
# 2. Add at least 3 entries to the dictionary, with people's names as the keys and their phone numbers as the values
# 3. Print out the phone number of one of the people in the dictionary
# 4. Change the phone number of one of the people in the dictionary
# 5. Print out all the keys and values in the dictionary using a loop, separated by a colon

phonebook = {}
phonebook["sam"] = 230
phonebook["tom"] = 418
phonebook["jan"] = 134 


print(phonebook["sam"])
phonebook["jan"] = 471 # what if i want to change the name to lara how ?

# for i in phonebook:
#     print(i , (phonebook["jan","sam","tom"])) # tries to print the value and key both together did not work

for i in phonebook:
    print(i)

# for i in phonebook.values():
#     print(values)    NOT WORKING 

#did't know this one
for i , value in phonebook.items():
    print(i , value) # can not put colon in " : "

