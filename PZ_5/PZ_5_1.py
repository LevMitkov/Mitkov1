def function():
    a = int(input())
    for i in range(0, a):           # Цикл для вывода с 1 (0) строки по строку a
        for a in range(0, i + 1):
            print('*', end='')
        print('')                   # Вывод звёздочек отдельно, построчно
function()