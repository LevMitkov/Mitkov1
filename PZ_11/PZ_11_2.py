import string

d = 0
for i in open('text18-17.txt', encoding='UTF-8'):
    print(i, end='')

# Подсчёт пунктуации
    for j in i:
        if j in string.punctuation:
            d += 1
print(end='\n')

print('Количество знаков препинания : ', d, end='\n')
f1 = open('text18-17.txt', encoding='UTF-8')
l = f1.readlines()
# Перемещаем последнюю строку на вторую позицию между первой и второй
l.insert(1, l[6])
l[1] = end = '\n'
l.insert(1, l[7])
l.pop(8)
f1.close()
f2 = open('text18-17-1.txt', 'w')
f2.writelines(l)
f2.close()
