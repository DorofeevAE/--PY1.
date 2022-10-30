dist_ = {}
def get_count_char(str_):

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



def get_simvols_char(dist_):
    dist_simvols = {}
    count_values = sum(dist_.values())
    for i in dist_:
        dist_simvols[i] = round(100 * dist_[i] / count_values, 2)
    return dist_simvols

print(get_simvols_char(dist_))




