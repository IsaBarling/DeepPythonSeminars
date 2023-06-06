number = int(input("Введите число от 1 до 999: "))

if 1 <= number <= 9:
    square = number ** 2
    print("Введена цифра:", number)
    print("Квадрат числа:", square)
elif 10 <= number <= 99:
    digit_product = (number // 10) * (number % 10)
    print("Введено двузначное число:", number)
    print("Произведение цифр числа:", digit_product)
elif 100 <= number <= 999:
    reverse_number = int(str(number)[::-1])
    print("Введено трехзначное число:", number)
    print("Зеркальное отображение числа:", reverse_number)
else:
    print("Число не входит в диапазон от 1 до 999. Пожалуйста, введите новое число.")
