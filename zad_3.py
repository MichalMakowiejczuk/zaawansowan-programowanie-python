def is_even(num) -> bool:
    return num % 2 == 0


result = is_even(7)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
