import sys

# for arg in sys.argv:
#     print(arg)

print(sys.argv)


def register():
    print("Start Register")
    email=input('Enter your email:')
    password=input('Enter your password:')
    print(f'Your email is {email} and password is {password}.\n You account has been created.')


def login():
    print("\n\nStart Login")
    email=input('Enter your email:')
    password=input('Enter your password:')
    print(f'Your email is {email} and password is {password}')



input = "  "
if input == "register" :
    print("register")
elif input == "login" :
    print("login")









    