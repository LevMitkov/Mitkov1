try:
    a = int(input())    # Ввод значений переменных
    b = int(input())
    while (a>=b):       # Пока первая переменная больше или равна второй - выполняеся цикл
        a -= b
    print(a)            # Вывод значения перменной a
except:
    print('Ошибка')

    # Добавил коментарии 12.11.22 в 00.35 (Забыл про них вначале, извиняюсь. Дату размещения PZ можно проверить по файлу init)
