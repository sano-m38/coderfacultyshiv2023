### Project tasks

# using pip install bcrypt

# 1. Implement a User class to represent a government agent. The User class should have attributes like agent ID, username, hashed password (using a strong encryption algorithm like bcrypt), and a list of encrypted tasks associated with the agent.
# 2. Allow agents to register an account with a unique agent ID, username, and password. The agent ID should be provided by the agency to ensure uniqueness and identification.
# 3. Use the **`cryptography`** library in Python to implement data encryption and decryption. Use AES encryption with a strong encryption key derived from the user's password.
# 4. Users should be able to:
#     - Add a new task to their list, including a task description, due date, and project classification level (e.g., Top Secret, Secret, Confidential).
#     - View all tasks in their list with the sensitive data redacted (e.g., task description and project classification).
#     - Decrypt and view sensitive task details (description and classification) only after successful authentication with a secure token (a one-time code provided by the agency).
# 5. Store user account information and encrypted tasks in separate files securely.




# import bcrypt

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = bcrypt.hashpw(password.encode, bcrypt.gensalt())


#     def add_task(self, task):
#         self.tasks.append(task)



#     def remove_task(self, task):
    

#         self.tasks.remove(task)

#     def verify_password(self, password):
#         return bcrypt.checkpw(password.encode, self.password)

# 














### Optional tasks
# 1. Use argparse module to handle command-line arguments and create a user-friendly command-line interface.
#     An example is shown below:
    
# ```bash
# $ python todo_manager.py register
# Username: john_doe
# Password: ********
# Account created successfully!

# $ python todo_manager.py login
# Username: john_doe
# Password: ********
# Login successful!
# ```

# 1. Design a mechanism to handle password resets with strong security checks to ensure the agent's identity.
# 2. Create a separate log file that records all user activities (e.g., login attempts, task updates) for auditing purposes, ensuring that this log file is also encrypted and accessible only to authorised personnel (implement authorisation_level attribute in the User class).

# <aside>
# ➡️ After developing the tool, you should upload it to github in a new repository.

# </aside>


# import argparse from ArgumentParser , Namespace 


# parser = ArgumentParser()

# parser.add_argument('register')

# args = parser.parse_args()

# print(args.echo)




# tryong example from yt video

from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square' , help = 'Squares a given number' , type=int)

arg: Namespace= parser.parse_args()

print(arg.square ** 2)      #problem with pylance not defining it  


# from argparse import ArgumentParser, Namespace

# parser = ArgumentParser()

# parser.add_argument('register')

# arg = parser.parse_args()

# print(arg.register)  









