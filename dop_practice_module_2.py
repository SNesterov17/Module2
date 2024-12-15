numbers_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numbers_1:
    numbers_2 = []
    for j in range(1, 20):
        for k in range(j + 1, 20): # добавлением 1 к j исключаем повторение пары чисел в обратной последовательности
            if i % (j + k) == 0:
                numbers_2.append(j)
                numbers_2.append(k)
    print(i, ' - ', *numbers_2, sep='')











