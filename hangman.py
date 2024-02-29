import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
    |
   ===''', '''
+---+
|   |
    |
    |
    |
   ===''', '''
+---+
|   |
0   |
    |
    |
   ===''', '''
 +---+
 |   |
(0   |
     |
     |
    ===''', '''
 +---+
 |   |
(0)  |
     |
     |
    ===''', ''' 
 +---+
 |   |
(0)  |
 |   |
     |
    ===''', '''
 +---+
 |   |
(0)  |
/|   |
     |
    ===''', '''
 +---+
 |   |
(0)  |
/|\  |
     |
    ===''', '''
 +---+
 |   |
(0)  |
/|\  |
/    |
    ===''', '''
 +---+
 |   |
(0)  |
/|\  |
/ \  |
    ===''']
words = {'Цвета': 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
         'Фигуры': '''квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник
         шестиугольник восьмиугольник'''.split(),
         'Фрукты': '''яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан
         нектарин'''.split(),
         'Животные': '''аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось
         медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек
         ящерица'''.split()}


def get_random_word(word_dict):
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return word_dict[word_key][word_index], word_key


def display_board(missed_leters, correct_leters, secret_word):
    print(HANGMAN_PICS[len(missed_leters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missed_leters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for _ in range(len(secret_word)):
        if secret_word[_] in correct_leters:
            blanks = blanks[:_] + secret_word[_] + blanks[_ + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    while True:
        print('Введите букву.')
        guesses = input().lower()
        if len(guesses) != 1:
            print('Пожалуйста, введите только одну букву')
        elif guesses in already_guessed:
            print('Вы уже называли эту букву. Введите другую.')
        elif guesses not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guesses


def play_again():
    print('Хочешь сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
print(HANGMAN_PICS[9])

difficulty = 'X'
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый')
    difficulty = input().upper()
    if difficulty == 'С':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[6]
    if difficulty == 'Т':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[6]
        del HANGMAN_PICS[4]
        del HANGMAN_PICS[2]

missed_leters = ''
correct_leters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print('Секретное слово из набора:', secret_set)
    display_board(missed_leters, correct_leters, secret_word)
    guesses = get_guess(missed_leters + correct_leters)

    if guesses in secret_word:
        correct_leters += guesses

        found_all_leters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_leters:
                found_all_leters = False
                break
        if found_all_leters:
            print('ДА! Секретное слово - "' + secret_word + '"! Вы угадали!')
            game_is_done = True
    else:
        missed_leters += guesses

        if len(missed_leters) == len(HANGMAN_PICS) - 1:
            display_board(missed_leters, correct_leters, secret_word)
            print('Вы исчерпали все попытки!\nНе угадано букв:', len(missed_leters))
            print('Угадано букв:', len(correct_leters))
            print('Осталось угадать: ', len(secret_word) - len(correct_leters))
            print('Было загадано слово "' + secret_word + '"')
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_leters = ''
            correct_leters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break
