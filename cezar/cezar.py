def cod_ru(rot, text):
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            if ord(text[i]) + rot > 1103:
                text[i] = chr(1072 + abs(1103 - (ord(text[i]) + rot - 1)))
            else:
                text[i] = chr(ord(text[i]) + rot)
        elif text[i].isalpha() and text[i].isupper():
            if ord(text[i]) + rot > 1071:
                text[i] = chr(1040 + abs(1071 - (ord(text[i]) + rot - 1)))
            else:
                text[i] = chr(rot + ord(text[i]))
    return ''.join(text)
    
def dec_ru(rot, text):
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            if ord(text[i]) - rot < 1072:
                text[i] = chr(1103 + (ord(text[i]) - 1072 - rot + 1))
            else:
                text[i] = chr(ord(text[i]) - rot)
        elif text[i].isalpha() and text[i].isupper():
            if ord(text[i]) - rot < 1040:
                text[i] = chr(1071 + (ord(text[i]) - 1040 - rot + 1))
            else:
                text[i] = chr(ord(text[i]) - rot)
    return ''.join(text)

def cod_en(rot, text):
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            if ord(text[i]) + rot > 122:
                text[i] = chr(97 + abs(122 - (ord(text[i]) + rot - 1)))
            else:
                text[i] = chr(ord(text[i]) + rot)
        elif text[i].isalpha() and text[i].isupper():
            if ord(text[i]) + rot > 90:
                text[i] = chr(65 + abs(90 - (ord(text[i]) + rot - 1)))
            else:
                text[i] = chr(rot + ord(text[i]))
    return ''.join(text)
    
def dec_en(rot, text):
    for i in range(len(text)):
        if text[i].isalpha() and text[i].islower():
            if ord(text[i]) - rot < 97:
                text[i] = chr(122 + (ord(text[i]) - 97 - rot + 1))
            else:
                text[i] = chr(ord(text[i]) - rot)
        elif text[i].isalpha() and text[i].isupper():
            if ord(text[i]) - rot < 65:
                text[i] = chr(90 + (ord(text[i]) - 65 - rot + 1))
            else:
                text[i] = chr(ord(text[i]) - rot)
    return ''.join(text)

choice = input(
    'Собираетесь расшифровать (введите "D") или зашифровать ("C") текст: ').lower()
language = input('Выберете язык "En" или "Ru": ').lower()
rot = int(input('Задайте шаг сдвига: '))
text = input(
    'Введите текст, который хотите расшифровать/зашифровать: ')
text = list(text)

if choice == 'c' and language == 'ru':
    print(cod_ru(rot, text))
elif choice == 'd' and language == 'ru':
    print(dec_ru(rot, text))
elif choice == 'c' and language == 'en':
    print(cod_ru(rot, text))
elif choice == 'd' and language == 'en':
    print(dec_ru(rot, text))

input('Отправьте любой символ для выхода из программы')