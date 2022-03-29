def privetsntvie(func):
    """Декоратор выдает приветствие и указывает в какую группу определен человек"""
    def wrapper():
        name = str(input("Enter you Name:"))
        print ("Hello!", name)
        func()
        print ('Nice to meet you!')
    return wrapper


@decorator1
def sort_lastname():
    """Функция сортирующая фамилии на группы согласно алфавитного порядка"""
    lastname = str(input("Enter you Lastname:"))
    if (lastname <= "K"):
        print("Your group is number 1")
    elif (lastname > "K" and lastname <= "S"):
        print("Your group is number 2")
    else:
        print("You group is number 3")
    return lastname


sort_lastname()











