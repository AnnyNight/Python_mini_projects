import random
def is_valid_cnt(num):
    while not(num.isdigit()) or int(num) < 1:
        num = input("Введено некорректное число. Попробуйте ещё\n")
    return int(num)

def is_valid_len(num):
    while not(num.isdigit()) or int(num) < 3:
        num = input("Введено некорректное число. Пароль должен быть не меньше 3х символов."
              "Попробуйте ещё\n")
    return int(num)

def valid_yn(text):
    while (text not in options_Y) and (text not in options_N):
        text = input("Неверный ввод. Повторите.\n")
    return text


def generator():
    need = []
    min_sym = 0
    cntPw = is_valid_cnt(input("Укажите количество паролей для генерации: \n"))
    lenPw = is_valid_len(input("Какой длины должен быть пароль?\n"))
    digOn = valid_yn(input("Включать ли цифры ? (да\нет)\n"))
    ABCon = valid_yn(input("Включать ли ПРОПИСНЫЕ буквы? (да\нет)\n"))
    abcOn = valid_yn(input("Включать ли строчные буквы? (да\нет)\n"))
    symbOn = valid_yn(input("Включать ли символы !#$%&*+-=?@^_? (да\нет)\n"))
    exOn = valid_yn(input("Исключать ли неоднозначные символы il1Lo0O? (да\нет)\n"))
    if digOn in options_Y:
        need += digits
        min_sym += 1
    if ABCon in options_Y:
        need += uppercase_letters
        min_sym += 1
    if abcOn in options_Y:
        need += lowercase_letters
        min_sym += 1
    if symbOn in options_Y:
        need += punctuation
        min_sym += 1
    if exOn in options_Y:
        for c in "il1Lo0O":
            need.remove(c)
    if min_sym == 0:
        print("Вы не выбрали никакие символы. Пароль создать не получится.")
        user_choice = input("Хотите попробовать ещё? (да/нет)\n")
        if user_choice in options_Y:
            generator()
        else:
            print("Вы вышли из генератора паролей.")
    else:
        print("Ваши пароли: ")
        for i in range(1, cntPw + 1):
            password = "".join([random.choice(need) for j in range(lenPw)])
            print(i, "пароль:",password)
        user_choice = input("Хотите попробовать ещё? (да/нет)\n")
        if user_choice in options_Y:
            generator()
        else:
            print("Вы вышли из генератора паролей.")



options_Y = ["д", "да", "Да", "yes", "Yes", "y"]
options_N = ["н", "нет", "Нет", "n", "no", "No"]

digits = [x for x in "0123456789"]
lowercase_letters = [x for x in "abcdefghijklmnopqrstuvwxyz"]
uppercase_letters = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
punctuation = [x for x in "!#$%&*+-=?@^_"]


print("Добро пожаловать в генератор паролей!")
generator()


