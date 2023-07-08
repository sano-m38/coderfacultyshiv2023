#1. Define a function named **`divide_numbers`** that takes two parameters, **`numerator`** and **`denominator`**.
# 2. Inside the function, write a **`try`** block that divides the **`numerator`** by the **`denominator`**.
# 3. If the division is successful, print the result to the console.
# 4. If the division fails due to an error, catch the exception and print a message to the console saying that an error occurred while performing the division. Then print the exception using `str(e)`
# 5. Call the **`divide_numbers`** function with the parameters 10 and 0 to test the **`ZeroDivisionError`** by dividing by 0.
# 6. Call the **`divide_numbers`** function with the parameters 10 and "hello" to test the exception handling for other types of exceptions.



def divide_numbers(numerator , denominator):
    try:                                                                                                            
        result = numerator / denominator                 # remember that need to put the block with error before writing except part 
    except Exception as e:                                                           
        print("an error occurred while performing the division " + str(e))               # don't forget to follow order 
    else:                                                                                
        print(result)                                                                    # try 
divide_numbers(10 , 0)                                                                   # except 
divide_numbers(10,5)                                                                     # else
divide_numbers(10,"hi")                                                                  # finally 