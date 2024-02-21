def search_value(my_list: list, target_value: int) -> bool:
    return target_value in my_list


my_list = [5, 7, 2, 1]

print(search_value(my_list, 1))
print(search_value(my_list, 3))