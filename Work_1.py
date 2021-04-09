# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.
# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
# что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.
# 4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
# и дочерний классы получили новое значение цены. Следует проверить это, вызвав
# соответствующий метод родительского класса и функцию дочернего
# (функция, отвечающая за отображение информации о товаре в одной строке).
# 5. Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).
# 6. Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def name_price_product(self):
        return [self.__name, self.__price]


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discount = discount

    def get_parent_data(self):
        return f"{self.name_price_product()[0]}: {self.name_price_product()[1]}"

    def __str__(self):
        return f"{(1 - self.discount / 100) * int(self.name_price_product()[1])}"


class ItemDiscountReportA(ItemDiscount):
    def get_info(self):
        return f"{self.name_price_product()[0]}"

    def __str__(self):
        return f"{self.get_info()}"


class ItemDiscountReportB(ItemDiscount):
    def get_info(self):
        return f"{self.name_price_product()[1]}"

    def __str__(self):
        return f"{self.get_info()}"


item_1 = ItemDiscount("Banana", 50)
item_2 = ItemDiscountReport(name="Apple", price=30)
# print(item_1.name,item_1.price)
print(item_2.get_parent_data())

# print(item_1.__name)

print(item_1.name_price_product()[0], item_1.name_price_product()[1])

item_1 = ItemDiscount("Grapes", 100)
item_2 = ItemDiscountReport(name="Tangerines", price=60)
print(item_1.name_price_product())
print(item_2.get_parent_data())

item_3 = ItemDiscountReport(name="Strawberry", price=150, discount=10)
print(item_3)

item_a = ItemDiscountReportA(item_1.name_price_product()[0], item_1.name_price_product()[1])
item_b = ItemDiscountReportB(item_1.name_price_product()[0], item_1.name_price_product()[1])
for some_class_instance in [item_a, item_b]:
    print(some_class_instance.get_info())
print(item_a.get_info(), item_b.get_info())
print(item_a, item_b)
