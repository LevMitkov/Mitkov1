# Дан словарь на 6 персон, найти и вывести их средний возраст. (Пример,
# {"Андрей": 32, "Виктор": 29, "Максим": 18, …}, среднее 26,33).

p_ages = {"Андрей": 32, "Виктор": 29, "Максим": 18, "Олег": 33, "Артём": 19, "Алексей": 42}

print(sum(p_ages.values())/6)   # Находим среднее арифметическое значений элементов списка