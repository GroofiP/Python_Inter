# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
# состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
import os
import random
import re
import string


def read_file(name_file):
    with open(f"{name_file}", "r") as f:
        a = f.read()
        print(a)
        b = re.findall(r"\w+\d+'", a)
        c = re.sub(r"\s\d\d", "Hello World", a)
        print(b)
        print(c)


def new_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print("Такой файл уже существует")
            break
    else:
        list_words = ["".join(random.choice(string.ascii_letters) for j in range(random.randint(4, 9))) for i in
                      range(random.randint(4, 9))]
        list_numbers = [random.randrange(1, 100) for i in range(random.randint(4, 9))]
        for i in range(0, len(list_words), 2):
            list_words[
                i] = f'{"".join(random.choice(string.ascii_letters) for j in range(6))}{random.randint(100, 999)}'
        numbers_words = list(zip(list_words, list_numbers))
        with open(f"{name}", "w") as f:
            for word in numbers_words:
                f.write(str(f"{word}\n"))
        read_file(name)


new_file("file_1.txt", "/home")

read_file("file_1.txt")
