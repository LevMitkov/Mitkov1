try:
    a = int(input())
    if a<0:
        print("Введено некорректное значение")
    else:
        print((a%10) * 100 + (a%100//10) * 10 + (a//100))
except:
    print("Ошибка")