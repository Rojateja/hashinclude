def merge(dict_1,dict_2):
    result = dict_1 | dict_2
    return result
dict_1 = {'john':'A','misa':'B'}
dict_2 = {'bonnie':'C','rick':'D'}
dict_3 = merge(dict_1,dict_2)
print(dict_3)
