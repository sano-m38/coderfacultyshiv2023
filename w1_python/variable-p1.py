"""
1. Define and initialise two variables
   a. name with the value `John`
   b. single with the value `False`
2. Define a variable age and request the user to input his age and assign it to the variable age.
3. Print out the values of the variables
    a. Output should be : 
        i. `My name is John`
        ii. `My age is 22`
4. Change the value of name to `Tom` and the value of single to `True`
5. Print the updated name
6. Print the name and the age in one single `print()` using string formatting
"""

name = "john"
single = "single" # i don't understand this single

age = 1   #problem i can input any  number or alphabet should i write an IF satement to limit the range or datatypes   

age =  input ("enter your age ")

#print ("my name is" , name , "and my age is" , age)
print ("my name is" , name )
print ("my age is" , age )


#did not know the end part 
# Change the value of a variable
name = "Tom"
age=22

# Print out the updated value
print("Name (updated):", name)

# Print both name and age
print("My name is {} and my age is {}".format(name, age))
