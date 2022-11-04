import string
from random import sample


def get_random_password() -> str:
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    list_ = [str(i) for i in range(9)]
    list_.append(upper)
    list_.append(lower)
    list_ = "".join(list_)
    password = sample(list_, 8)
    return password



# TODO написать функцию генерации случайных паролей


print(get_random_password())
