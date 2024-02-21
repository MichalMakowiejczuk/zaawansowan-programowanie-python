def list_operations(list1: list, list2: list) -> list:
    result_list = list(set(list1 + list2))
    result_list = [i ** 3 for i in result_list]
    return result_list


list1 = list(range(6))
list2 = list(range(3, 10))

print(list_operations(list1, list2))
