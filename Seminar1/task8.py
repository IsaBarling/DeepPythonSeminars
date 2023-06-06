rows = int(input("Сколько рядов у ёлки? "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
