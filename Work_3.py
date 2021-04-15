# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
# в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.

list_key = ["sugar", "apple", "orange", "chocolate", "answer", "computer", "notebook", "milk"]
list_value = [1, 2, 3, 4, 5]


def dict_list(list_a, list_b):
    dict_a = {}
    a = list(zip(list_a, list_b))
    for k, v in a:
        dict_a[k] = v
    if len(list_a) > len(list_b):
        number = len(list_b) - len(list_a)
        number = list_a[number:]
        for k in number:
            dict_a[k] = None
    return dict_a


print(dict_list(list_key, list_value))
