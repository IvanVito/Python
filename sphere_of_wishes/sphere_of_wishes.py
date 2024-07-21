import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, я магический шар, и я помогу ответить на любой твой вопрос.')
name = input('Представьтесь: ')
print(f'Очень приятно, {name}')

def main_body():
    print('Задай вопрос, на который ты хочешь получить ответ :')
    qustion = input()
    print('Ответ:', random.choice(answers))

def end():
    new_session = input(
        'Остались ли у тебя еще вопросы ? (введи "Да" или "Нет"): ')
    new_session = new_session.lower()
    while new_session != 'да' and new_session != 'нет':
        new_session = input(
            'Да или нет ?: ')
        new_session = new_session.lower()
    if new_session != 'да':
        print('Возвращайся если возникнут вопросы!')
    return new_session

main_body()
while end() == 'да':
    main_body()