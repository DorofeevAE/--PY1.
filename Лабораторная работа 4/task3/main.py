def delete(list_, index=None):
    if index is not None and len(list_) > index > -1:
        a = list_[:index]
        b = list_[index+1:]
        end_ = a + b
        return end_
    else:
        list_ = list_[:-1]
        return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
# Дополнительные условия
print(delete([0, 0, 1, 2], index=0)) # [0, 1, 2]
print(delete([0, 1, 2, 3], index=6)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-1)) # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4], index=-6)) #[0, 1, 2, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-3)) #[0, 1, 3, 4]
print(delete([0, 1, 2, 3, 4], index=-2)) #[0, 1, 2, 4]
print(delete([0, 1, 2, 3, 4, 5])) # [0, 1, 2, 3, 4]