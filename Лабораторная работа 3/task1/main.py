src = not False and True or False and not True


# TODO расписать упрощение выражения
# src = True and True or False and False # Избавляемся от отрицаний
# scr = True or False # Избавляемся от логического оператора "И"
# scr = True  # избавляемся от логического "ИЛИ"
result = True  # TODO подставить результат выражения

print(src == result)
