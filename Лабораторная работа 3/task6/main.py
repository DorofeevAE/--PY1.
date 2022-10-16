list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
# Находим индекс максимального элемента (max_value - максимальное значение, current_value - текущее значение в цикле, max_index - максимальный индекс)
for i in range(len(list_numbers)):
    max_value = list_numbers[max_index]
    current_value = list_numbers[i]
    if current_value > max_value:
        max_index = i

# Меняем значения местами
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
