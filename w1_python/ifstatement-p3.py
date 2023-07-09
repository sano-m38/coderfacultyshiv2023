"""
1. Define a variable **`name`** and request the user to input their name.
2. Write an if statement to check if the name is "Alice". If true, print "Welcome Alice!". 
3. Otherwise, print "You are not Alice. Please enter the correct name".
4. Update your program to also  check if the name is "Bob". If true, print "Welcome Bob!"
"""

name = input ("please enter your name ")
if name == ("Alice") : # this colon is important it will indent the print automatically also it represent Then
       print ("Welcom alice")
else: 
       print ("you are not alice please enter correct name")

name = input ("please enter your name ")
if name == ("Bob") :
       print ("Welcom bob")
else:
       print ("you are not bob please enter correct name")