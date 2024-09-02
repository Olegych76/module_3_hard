def count_data(*args):
    global string_count

    for arg in args:
        # проверяем последовательность arg на принадлежность к словарю, списку, кортежу, множеству, простым данным...:
        if isinstance(arg, dict):
            for key, value in arg.items():
                #  обрабатываем key:
                if isinstance(key, (int, float)):
                    string_count += key  # если ключ - цифровой
                elif isinstance(key, str):
                    string_count += len(key)  # если ключ - строка
                #  обрабатываем value
                count_data(value)  # вызываем эту же функцию рекурсивно
        elif isinstance(arg, (list, tuple, set)):  # если arg - список, кортеж, множество:
            for elem in arg:  # обрабатываем каждый элемент последовательности:
                count_data(elem)  # вызываем эту же функцию рекурсивно
        elif isinstance(arg, (int, float)):  # если arg - число
            string_count += arg
        elif isinstance(arg, str):  # если arg - строка
            string_count += len(arg)

    return


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

string_count = 0

count_data(data_structure)
print("Сумма всех данных:", string_count)
