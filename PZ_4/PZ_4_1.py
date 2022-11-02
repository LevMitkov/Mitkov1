try:
    n = int(input())
    s = 0.0
    for i in range(1, n + 1):
        s += 1.0 / i
    print(s)
except:
    print("Ошибка")
