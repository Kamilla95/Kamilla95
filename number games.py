import random

print('*' * 10, 'Угадай число v 1.0', '*' * 10)
print('Компьютер загадает число от 1 до 100. Попробуйте угадать!')

answer = 1
score = 0
i = 0

while answer:
    if answer == 0:
        break

    rand = random.randint(1, 100)
    answer = int(input('Число загадано. Попробуйте отгадать: '))
    if answer == rand:
        score += 1
        print('Ты угадал!')
    else:
        print('Ты не угадал! Пробуй еще! Было загадано: ', rand)
    i += 1
print('Всего отгадано чисел: ', score, 'из', i)
print('Приходи ещё')
input('Для вызова нажми Enter!')
