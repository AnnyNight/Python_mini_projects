def caesar_cipher():
    direction = valid_direction(input("Выберите направление: (шифрование/дешифрование)\n"))
    user_txt = valid_text(input("Введите текст:\n"))
    k = valid_num(input("Введите шаг сдвига:\n"))
    language = valid_lang(input("Какой язык вы используете? (рус/англ)\n"))
    if direction == "шифрование":
        if language == "рус":
            print(shifrovka(user_txt, k, rus_alph))
        elif language == "англ":
            print(shifrovka(user_txt, k, eng_alph))
    else:
        if language == "рус":
            print(deshifrovka(user_txt, k, rus_alph))
        elif language == "англ":
            print(deshifrovka(user_txt, k, eng_alph))
    user_choice = input("Хотите повторить? (да/нет)\n")

    if user_choice in ["да", "д", "Да", "y", "yes"]:
        caesar_cipher()
    else:
        print("Вы вышли.")


# шифрование
def shifrovka(user_txt, k, lang):
    res = ""
    length = len(lang)
    for i in range(len(user_txt)):
        if user_txt[i].lower() not in lang:
            res += user_txt[i]
            if res.isalpha():
                return "Введенный текст не соответствует языку. Повторите попытку"
            continue
        ind_alph = lang.index(user_txt[i].lower())
        if user_txt[i].isupper():
            res += lang[(ind_alph + k) % length].upper()
        else:
            res += lang[(ind_alph + k) % length]
    return res

# дешифрование
def deshifrovka(user_txt, k, lang):
    result = ""
    length = len(lang)
    for i in range(len(user_txt)):
        if user_txt[i].lower() not in lang:
            result += user_txt[i]
            continue
        ind_alph = lang.index(user_txt[i].lower())
        if user_txt[i].isupper():
            result += lang[(ind_alph - k) % length].upper()
        else:
            result += lang[(ind_alph - k) % length]
    return result

# проверка на корректность текста
def valid_text(txt):
    while txt == "" or  txt.isspace():
        print("Некорректный ввод. Попробуйте ещё")
        txt = input()
    if "ё" in txt:
        txt = txt.replace("ё", "е")
    if "Ё" in txt:
        txt = txt.replace("Ё", "Е")
    return txt

# проверка на корректность направления
def valid_direction(txt):
    while txt not in ["шифрование", "дешифрование"]:
        print("Некорректный ввод. Выберите 'шифрование' или 'дешифрование'")
        txt = input()
    return txt

# проверка на корректность шага сдвига
def valid_num(num):
    while not(num.isdigit()):
        print("Некорректный ввод. Введите число")
        num = input()
    return int(num)

# проверка на корректность ввода языка
def valid_lang(lang):
    while lang not in ["англ", "рус"]:
        print("Некорректный ввод. Выберите язык: 'англ' или 'рус'")
        lang = input()
    return lang


eng_alph = "abcdefghijklmnopqrstuvwxyz"
rus_alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

print("Программа шифровки / дешифровки текста по методу Цезаря")
# caesar_cipher()
