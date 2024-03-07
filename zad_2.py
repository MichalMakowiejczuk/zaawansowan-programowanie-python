def multiply_by_2_loop(list_of_ints):
    result = []
    for i in list_of_ints:
        result.append(i*2)
    return(result)


def multiply_by_2_comprehension(list_of_ints):
    result = [i*2 for i in list_of_ints]
    return(result)


test_ints = list(range(1, 6))
print(multiply_by_2_loop(test_ints))
print(multiply_by_2_comprehension(test_ints))
