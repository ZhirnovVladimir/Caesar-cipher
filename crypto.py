def crypt_eng():
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                index = eng_lower_alphabet.find(text[i]) + step
                if index >= len(eng_lower_alphabet):
                    index = index - len(eng_lower_alphabet)  # - 1
                elif index < 0:
                    index = len(eng_lower_alphabet) + index  # + 1
                result += eng_lower_alphabet[index]
            elif text[i].isupper():
                index = eng_upper_alphabet.find(text[i]) + step
                if index >= len(eng_upper_alphabet):
                    index = index - len(eng_upper_alphabet)  # - 1
                elif index < 0:
                    index = len(eng_upper_alphabet) + index  # + 1
                result += eng_upper_alphabet[index]
        else:
            result += text[i]
    return result


def crypt_ru():
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].islower():
                index = rus_lower_alphabet.find(text[i]) + step
                if index >= len(rus_lower_alphabet):
                    index = index - len(rus_lower_alphabet)  # - 1
                elif index < 0:
                    index = len(rus_lower_alphabet) + index  # + 1
                result += rus_lower_alphabet[index]
            elif text[i].isupper():
                index = rus_upper_alphabet.find(text[i]) + step
                if index >= len(rus_upper_alphabet):
                    index = index - len(rus_upper_alphabet)  # - 1
                elif index < 0:
                    index = len(rus_upper_alphabet) + index  # + 1
                result += rus_upper_alphabet[index]
        else:
            result += text[i]
    return result


def decrypt_ru():
    for a in range(1, 33):
        result = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].islower():
                    index = rus_lower_alphabet.find(text[i]) - a
                    if index < 0:
                        index = len(rus_lower_alphabet) + index  # + 1
                    result += rus_lower_alphabet[index]
                elif text[i].isupper():
                    index = rus_upper_alphabet.find(text[i]) - a
                    if index < 0:
                        index = len(rus_upper_alphabet) + index  # + 1
                    result += rus_upper_alphabet[index]
            else:
                result += text[i]
        print('Ключ шифровани:', a)
        print(result)


def decrypt_en():
    for a in range(1, 27):
        result = ''
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].islower():
                    index = eng_lower_alphabet.find(text[i]) - a
                    if index < 0:
                        index = len(eng_lower_alphabet) + index  # + 1
                    result += eng_lower_alphabet[index]
                elif text[i].isupper():
                    index = eng_upper_alphabet.find(text[i]) - a
                    if index < 0:
                        index = len(eng_upper_alphabet) + index  # + 1
                    result += eng_upper_alphabet[index]
            else:
                result += text[i]
        print('Ключ шифровани:', a)
        print(result)


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
direction = input(
    'Что необходимо сделать? Шифровать или Дешифровать? ').lower()
language = input('Выберете язык (русский, английский) ').lower()
text = input('Введите текст ')
if direction == 'дешифровать':
    know = input('Занаете ли вы шаг шифрования (да, нет) ').lower()
    if know == 'да':
        step = int(input('Выеберете шаг шифрования '))
        step = step * (-1)
    elif know == 'нет':
        if language == 'русский':
            decrypt_ru()
        elif language == 'английский':
            decrypt_en()

elif direction == 'шифровать':
    step = int(input('Выеберете шаг шифрования '))
    if language == 'русский':
        print(crypt_ru())
    elif language == 'английский':
        print(crypt_eng())
