# 1. Create a new file called **`my_file.txt`** and write the following content to it:
#     
#     Hello, this is a sample text file.
#  
# 2. Open the file in **read mode** and print the contents of the file to the console.
# 3. Open the file in **append mode** and add the following line to the end of the file:
#     
#     This line is appended to the end of the file.
#     
# 4. Open the file again in read mode and print the contents of the file to the console to verify that the new line was added.
# 5. Close the file.
# 6. Make sure to handle any exceptions that may occur when opening and writing to the file.

file = open('file_testcode1.txt' , 'r')
print(file.read())                        #make sure when writing code the txt.file is not in the same folder as the code applicable also in file explora. otherwise the file not found

file = open('file_testcode1.txt', 'a')
print(file.write('this line is appened to the end of the file')) 

file = open('file_testcode1.txt' , 'r')
print(file.read())

file.close()

# why is the text continues to increase when running multiple times 