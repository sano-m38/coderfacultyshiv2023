# 1. The program should prompt the user to enter the number of subjects.
# 2. Using a loop, ask the user to enter the marks for each subject.
# 3. Calculate the total score by summing up all the marks.
# 4. Based on the total score, determine the corresponding letter grade using the following criteria:
#     - 90 or above: A
#     - 80-89: B
#     - 70-79: C
#     - 60-69: D
#     - Below 60: F
# 5. Display the total score and the corresponding letter grade to the user as output.


print ( 'welcome to simple grade calculator ! \n' )

numberofsubjects = int(input("enter number of the subjects: "))
print  ( "how many subjects do you have ? {} \n " .format(numberofsubjects))

total = 0
for i in range (numberofsubjects):
        mark = int(input(f"enter the mark for subject {i+1}: ")) 
        total = total + mark


print("\ntotal score:" , str(total))
avg=total/numberofsubjects

if avg >= 90:
        print("letter grade: A")

elif avg >= 80 and avg <= 89:
        print("letter grade: B")

elif avg >= 70 and avg <= 79:
        print("letter grade: C")

elif  avg  >=60 and avg <= 69:
        print("letter grade: D")

elif avg <60:
        print ("letter grade 4: F")
