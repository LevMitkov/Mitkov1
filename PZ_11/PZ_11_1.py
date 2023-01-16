# Запишем в файл data_1.txt структуру данных - список
l = ['-9 6 3']
lst = list(map(int, l[0].split()))
f1 = open('data_1.txt', 'w')
f1.writelines(l)
f1.close()

# Дублируем список в новый файл data_2.txt
f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(l)
f2.close()

# разбиваем строку и ее значения преобразуем в числа
f1 = open('data_1.txt')
k = f1.read()
k = k.split()
f1.close()

# в файле data_1.txt и записываем в файл data_2.txt
f1 = open('data_1.txt')
p = f1.read()
p = p.split()
print(type(p))

# Ищем произведение элементов
n = 1
for i in lst:
    n *= i
f1.close()

# Ищем количество пар, для которых произведение элементов делится на 3
b = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if (lst[i] * lst[j]) % 3 == 0:
            b += 1

f2 = open('data_2.txt', 'a')  # открываем файл для дозаписи
f2.write('\n')
print('Количество элементов:', len(k), file=f2)
print('Произведение элементов:', n, file=f2)
print('Количество пар, для которых произведение элементов делится на 3:', b, file=f2)
f2.close()