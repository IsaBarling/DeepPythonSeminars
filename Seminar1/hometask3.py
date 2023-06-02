from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

# Генерирация случайного числа
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от", LOWER_LIMIT, "до", UPPER_LIMIT)

# Переменная для счетчика попыток / пыток :)
attempt = 1

while attempt <= 10:
    guess = int(input("Попытка {}: Введите ваше предположение: ".format(attempt)))

    if guess < num:
        print("Загаданное число больше вашего предположения.")
    elif guess > num:
        print("Загаданное число меньше вашего предположения.")
    else:
        print("Поздравляю! Вы угадали число!")
        break

    attempt += 1

if attempt > 10:
    print("Вы исчерпали все попытки. Загаданное число было:", num)
