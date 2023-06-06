num = int(input("Введите число: "))

# Проверяем ограничения на ввод
if num < 2 or num > 100000:
    print("Число должно быть больше 1 и не превышать 100000.")
else:
    is_prime = True

    # Проверяем делители числа от 2 до корня из числа
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # Выводим результат
    if is_prime:
        print("Число", num, "является простым.")
    else:
        print("Число", num, "является составным.")
