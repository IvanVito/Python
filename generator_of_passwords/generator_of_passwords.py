import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
qantity_of_pas = int(input('Введите количество генерируемых паролей: '))
length_of_pas = int(input('Введите требуемую длину генерируемых паролей: '))
include_num = input(
    'Должен ли пароль включать цифры ? ("да", а если "нет", то любой символ): ').lower()
include_uplet = input(
    'Должен ли пароль включать строчные буквы ?: ').lower()
include_lowlet = input(
    'Должен ли пароль включать прописные буквы ?: ').lower()
include_punctuation = input(
    'Должен ли пароль включать знаки пунктуации ?: ').lower()
exept = input(
    'Должен ли пароль исключать неоднозначные символы (il1Io0O) ?: ').lower()

if include_num == 'да':
    chars += digits
if include_uplet == 'да':
    chars += uppercase_letters
if include_lowlet == 'да':
    chars += lowercase_letters
if include_punctuation == 'да':
    chars += punctuation
if exept == 'да':
    for i in 'il1Io0O':
        chars = chars.replace(i, '')
        

def generate_password(length_of_pas, chars):
    password = ''
    for _ in range(length_of_pas):
        password += random.choice(chars)
    return password

def quantity():
    count = 0
    while count != qantity_of_pas:
        print(generate_password(length_of_pas, chars))
        count += 1
        
quantity()
again = input(
    'Сгенерировать еще раз ? ("да", а если нет, то любой символ): ').lower()

while again == 'да':
    quantity()
    again = input(
        'Сгенерировать еще раз ? ("да", а если нет, то любой символ): ').lower()
