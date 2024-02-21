def get_even_numbers(list_of_ints):
    return list_of_ints[::2]


test_ints = list(range(10))
print(get_even_numbers(test_ints))