
# def decorator_regisr(func):
#     def wrapper():
#         func() 
#     return wrapper


new_file = open ('users.txt', "w")
# @decorator_regisr
def registration ():
    user = input("Login:")
    password = input("Password:")
    new_file.write(f'{user}:{password}''\n')
    return 
    

registration()
new_file.close


new_file = open ("users.txt", "r")
read_users= new_file.read()

def autorization():
    login = input("enter your login:")
    passw = input("enter your password:")
    if login in read_users and passw in read_users:
        print("Successfully")
    else:
        print("Incorrect login or password")
autorization()

new_file.close