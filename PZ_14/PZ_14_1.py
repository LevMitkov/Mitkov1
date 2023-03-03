# Из исходного текстового файла (experience.txt) выбрать стаж работы. Посчитать
# количество полученных элементов.
import re

with open('experience.txt', 'r', encoding='utf-8') as file:
    data: str = file.read()

print(*re.findall(r"(\d+ \w+)\s?(\d+ месяц.*$)?", data, re.M), sep='\n')
print("Количество полученных элементов: ", len(re.findall(r"(\d+ \w+)\s?(\d+ месяц.*$)?", data, re.M)))
