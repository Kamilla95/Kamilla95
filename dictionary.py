dict = {
    'apple' : 'Яблоко',
    'bold' : 'Жирный',
    'cat' : 'Кошка'
}

print('=' * 10, 'Словарь v 1.0', '=' * 10)
help = '''
s - Поиск слова по словарю
a - Добавить новое слово
r - Удалить слово
k - Вывод всех ключей в словаре
d - Вывод всего словаря
h - Вывод меню
q - Выход
'''

choice = ''
while choice != 'q':
    choice = input('(h - Справка >>) ')
    if choice == 's':
        word = input('Введите слово: ')
        res = dict.get(word, 'Нет такого слова!')
        print(res)
    elif choice == 'a':
        word = input('Введите слово: ')
        value = input('Введите перевод: ')
        dict[word] = value
        print('Слово добавлено!')
    elif choice == 'r':
        word = input('Введите слово: ')
        del dict[word]
        print('Слово ', word, ' удалено')
    elif choice == 'k':
        print(dict.keys())
    elif choice == 'd':
        for i in dict:
            print(i, ': ', dict[i])
    elif choice == 'h':
        print(help)
    elif choice == 'q':
        continue
    else:
        print('Нераспознанная команда. Введите h для вывода меню')

