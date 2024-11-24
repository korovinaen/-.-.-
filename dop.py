# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    count = 0
    for element in l:
        if element == item:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 1, 4, 1, 5]
print(my_count(my_list, 1))  # Вывод: 3
print(my_count(my_list, 2))  # Вывод: 1
print(my_count(my_list, 6))  # Вывод: 0