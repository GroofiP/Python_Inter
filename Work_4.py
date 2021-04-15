# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие файла
# и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
import os
import random
import string


def read_file(name_file):
    with open(f"{name_file}", "r") as f:
        print(f.read())


def new_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print("Такой файл уже существует")
            break
    else:
        list_words = ["".join(random.choice(string.ascii_letters) for j in range(random.randint(4, 9))) for i in
                      range(5)]
        list_numbers = [random.randrange(1, 100) for i in range(5)]
        numbers_words = list(zip(list_words, list_numbers))
        with open(f"{name}", "w") as f:
            for word in numbers_words:
                f.write(str(f"{word}\n"))
        read_file(name)


new_file("file_1.txt", "/home")

read_file("file_1.txt")
