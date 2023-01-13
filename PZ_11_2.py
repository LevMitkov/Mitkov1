import string

t = 0
d = 0
for i in open('text18-17.txt', encoding='UTF-8'):
 print(i, end='')
 t += 1
 for j in i:
    if j in string.punctuation:
        d+=1
print(end='\n')

print('Количество строк: ', t, end='\n')
print('Количество знаков препинания : ', d, end='\n')
f1 = open('text18-17.txt', encoding='UTF-8')
l = f1.readlines()
l[6], l[1] = l[1], l[6]
f1.close()
f2 = open('text18-17-1.txt', 'w')
f2.writelines(l)
f2.close()

