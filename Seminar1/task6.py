year = int(input("Введите год: "))

if year % 4 != 0:
    print(year, "не является високосным годом.")
elif year % 100 != 0:
    print(year, "является високосным годом.")
elif year % 400 != 0:
    print(year, "не является високосным годом.")
else:
    print(year, "является високосным годом.")
