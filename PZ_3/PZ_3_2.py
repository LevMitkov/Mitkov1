try:
    a = float(input())
    b = float(input())
    c = float(input())
    if (a > b) and (b > c):
        a = -a
        b = -b
        c = -c
        print(a, b, c)
    else:
        a = a * 2
        b = b * 2
        c = c * 2
        print(a, b, c)
except:
    print('Ошибка')
