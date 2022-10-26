dist_ = {}
def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for i in str_:
        if i.isalpha():
            dist_[i] = dist_.get(i, 0) + 1
    return dist_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dist_simvols = {}
def get_simvols_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for i in str_:
        if i.isalpha() is False:
            dist_simvols[i] = dist_simvols.get(i, 0) + 1
    count_values = sum(dist_simvols.values())
    for i in dist_simvols:
        dist_simvols[i] = (dist_simvols.get(i) * 100) / count_values
    return dist_simvols

#print(get_simvols_char(main_str))


