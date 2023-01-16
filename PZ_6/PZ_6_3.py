import random
k = random.randrange(1, 5)      # Генерируется случайное целое число в заданном промежутке
n = random.randrange(k+1, 21)
print("N = ", n)

a = [i+1 for i in range(n)]     # Генерируется список, заполненный числами от 1 до n в порядке возрастания
print(a)
print(a[k:] + a[:k])

b = []
for i in range(0, k):           # Формируется список с числами, которые займут последние позиции при переносе
    b.append(a[i])

for i in range(0, n-k):         # Числа, которые не переносятся, увеличиваются на индекс сдвига
    a[i] = a[i+k]

g = 0
for i in range(n-k, n):         # в лист заносятся числа, которые были перенесены вперёд
    a[i] = b[g]
    g += 1

print(a)