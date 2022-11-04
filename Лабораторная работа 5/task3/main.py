import random


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while True:
        try:
            int_ = random.randint(-10, 10)
            if int_ not in list_:
                list_.append(int_)
        except ValueError:
            continue
        finally:
            if len(list_) == 15:
                break
    return list_

# TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
