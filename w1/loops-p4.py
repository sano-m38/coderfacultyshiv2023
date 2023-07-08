"""
1. Loop through the list of numbers from 1 to 10 and print out each number
2. Loop through the list and print out only even numbers
3. Loop through the list and calculate the sum of all numbers
4. Loop through the list and calculate the average of all numbers
"""

#forgot to put the 
for number in range(1,11):
    print(number)

# question how can i display the name 10 times and not the numbers
# the i is a counter important 
# for i in range (11):
#     print ('sam')

# did not know those part
for i in range(11):
     if i % 2 == 0:
        print(i)

total = 0
for i in range(11):
    total += i
print(total)

total = 0
for number in range(1,11):
    total += number
average = total/10
print(average)

