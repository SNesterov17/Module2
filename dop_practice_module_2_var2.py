n = []
def numbers():
    n = int(input('Введите число "n", от 3 до 20:'))
    numbers_2 = []
    for j in range(1, 20):
        for k in range(j + 1, 20):  # добавлением 1 к j исключаем повторение пары чисел в обратной последовательности
            if n % (j + k) == 0:
                numbers_2.append(j)
                numbers_2.append(k)
    print(n, ' - ', *numbers_2, sep='')
numbers()