e = 2
n = 20

sum_even = 0
i = 1

while i <= n:
    if i % 2 == 0 and i % e != 0:
            sum_even += i
    i += 1

print("Сумма четных элементов от 1 до", n, "исключая кратные", e, ":", sum_even)

