def my_func(list_of_ints):
    return list_of_ints[::2]


test_ints = list(range(10))
print(my_func(test_ints))
