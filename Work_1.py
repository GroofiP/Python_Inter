# Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.

def multiplication_table(a, b):
    """Функция вывода таблицы умножения AxB"""
    for i in range(1,a+1):
        for y in range(1,b+1):
            print(f"{i}*{y}={i*y}")


multiplication_table(3,3)