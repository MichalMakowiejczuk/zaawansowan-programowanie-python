def get_even_numbers(list_of_ints):
    result = [i for i in list_of_ints if i%2==0]
    return result


test_ints = list(range(10))
print(get_even_numbers(test_ints))