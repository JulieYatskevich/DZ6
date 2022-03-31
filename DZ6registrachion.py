
def decorator_regisr(func):
    """Декоратор проверяет длинну пароля, 
    содержатся ли в нем специальные символы 
    и заглавные буквы """
    def wrapper(user, password):
        if len(password) < 8:
            raise Exception("Incorrect password length")
        simv = ". ? , ! * - + /"
        for simbol in simv:
            if simbol in password:
                raise Exception("The special symbol in the password")
            
        for letter in password:
            if letter.isupper():
                raise Exception ("Dont use upper letters")
        func(user, password) 
    return wrapper


new_file = open('users.txt', "a")

@decorator_regisr
def registration (user, password):
    """Функция регистрации пользователя и пароля"""
    new_file.write(f'{user}:{password}''\n')
    return 

user = input("Login:")
password = input("Password:")
    

registration(user, password)
new_file.close()


new_file = open ("users.txt", "r")
read_users= new_file.read()

def autorization():
    """Функция авторизации.
    Проверяет есть ли логин и пароль в документе users.txt"""
    login = input("Enter your login:")
    passw = input("Enter your password:")
    x = f'{login}:{passw}'
    print(x)
    if x in read_users:
        print("Successfully")
    else:
        print("Incorrect login or password")
autorization()

new_file.close()