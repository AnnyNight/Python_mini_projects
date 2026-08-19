import random
import time

print("Добро пожаловать в угадайку чисел!")
name = input("Как ваше имя?\n")
print(f"Ну что же, {name}, давай начнём!")

def start_valid(x):
    while not(x.isdigit() and int(x) > 0):
        time.sleep(0.5)
        print("Опа, ошибочка. Введите число заново")
        x = input()
    return int(x)

def end_valid(x, y):
    while not(y.isdigit() and int(y) > 0 and int(y) > int(x)):
        time.sleep(0.5)
        print("Опа, ошибочка. Введите число заново")
        y = input()
    return int(y)

def start():
    print("Выбери начало: ")
    open = input()
    open = start_valid(open)
    print("Выбери конец: ")
    end = input()
    end = end_valid(open, end)
    num0 = random.randint(open, end)
    print(f"Это число от {open} до {end}")
    user_num = input("Какое число я загадал?\n")
    user_num = start_valid(user_num)

    while user_num != num0:
        if open <= user_num < num0:
            time.sleep(0.5)
            print("Слишком мало, попробуйте еще раз")
        elif end >= user_num > num0:
            time.sleep(0.5)
            print("Слишком много, попробуйте еще раз")
        elif user_num > end or user_num < open:
            time.sleep(0.5)
            print("Вы перешли предел, так нечестно")
        user_num = start_valid(input())

    time.sleep(0.5)
    print("Вы угадали, поздравляем!")
    ans = input("Хотите сыграть ещё?\n")
    if ans in ["Да", "да", "lf"]:
        time.sleep(0.5)
        print("Отлично! Продолжаем")
        start()
    else:
        time.sleep(0.5)
        print("Тогда удачи!")


start()