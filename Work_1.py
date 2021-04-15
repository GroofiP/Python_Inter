# 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла,
# а затем «выделение» из этого пути имени файла (без расширения).
import os


def find(name):
    for root, dirs, files in os.walk("/home"):
        if name in files:
            name = name.split(".")[0]
            return f"Полный путь до файла: {root} \nИмя файла: {name}"


print(find("file.txt"))


# Я сначала решил как понял, а потом увидел ваш ответ в личке, как надо решать

def file_name_from_full_path(path):
    path = path.split("/")
    return path[-1].split(".")[0]


print("Имя файла:", file_name_from_full_path("/home/groofi/Work_Git/Python_Inter/file.txt"))
