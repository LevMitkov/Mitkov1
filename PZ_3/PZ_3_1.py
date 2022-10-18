try:
    a = int(input())
    if a < 0:
        print('Введите положительное число')
    else:
        if (a > 9) and (a < 100) and (a % 2 != 0):
             print('false')
        else:
             print('true')
except:
    print('Ошибка')