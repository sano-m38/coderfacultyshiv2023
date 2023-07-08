# 1. Create an empty list called fruits
# 2. Add the following items to the list using the append() method: apple , banana , orange
# 3. Print the length of the list using the len() function
# 4. Print the second item in the list
# 5. Change the value of the second item to grape
# 6. Print the entire list using a loop
# 7. Remove the first item from the list using the pop() method
# 8. Print the updated list


fruit = []
fruit.append("apple") #why i can not write fruit .append("apple , banana , orange") and execute it from there
fruit.append("banana") # otherwise it is not working print(fruit[2])
fruit.append("orange")

print (len(fruit)) # why is it giving me 1, is it supposed to print apple ,banana , orange or the list

print(fruit[2])

fruit[2] = "grape" #not changing to grape in interactive tab but it is in jupyter terminal why?

for item in fruit:
    print (item) #when plcing fruits in() it is preing ["apple" , "banana" , "grape"] x3 why 

fruit.pop(0)

print("updated list" , fruit)

