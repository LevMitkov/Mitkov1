try:
    a = float(input())      # Ввод значений переменных
    b = float(input())
    c = float(input())
    if (a > b) or (b > c): # Проверка на упорядоченность по возрастанию
        a = -a             # Присваиваем противоположные значения
        b = -b
        c = -c
        print(a, b, c)
    else:
        a = a * 2          # Присваиваем значения в 2 раза больше
        b = b * 2
        c = c * 2
        print(a, b, c)
except:
    print('Ошибка')
