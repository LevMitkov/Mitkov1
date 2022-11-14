import random        # Подключаю библиотеку random
try:                 # Делал проверку для ввода значений списка с клавиатуры
    ListAppend = []  # Пустой список, который мы будем заполнять
    s = 0
    i = 0
    while i < 10:    # Цикл выполняется пока переменная меньше 10
        ListAppend.append(random.randint(1, 10))    # Ввод рандомных 10 значений в список
        i += 1
except:
    print("Ошибка")
print(ListAppend)    # Вывод списка в консоль

for i in range(10):  # Цикл повторяется 10 раз
    if ListAppend[i] < ListAppend[9]:   # Условие подбора искомого элемента списка
        s = i
        break                           # Прерываем цикл после первого совпадения с условием

if ListAppend[s] >= ListAppend[9]:      # Условие, если нет совпадения с условием первого фильтра
    print(0)
else:
    print(ListAppend[s])
