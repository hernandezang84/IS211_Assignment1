class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    return len([num for num in numbers if num % divide == 0])

def test_list_divide():
    tests = [
        (list_divide([1, 2, 3, 4, 5]), 2),
        (list_divide([2, 4, 6, 8, 10]), 5),
        (list_divide([30, 54, 63, 98, 100], divide=10), 2),
        (list_divide([]), 0),
        (list_divide([1, 2, 3, 4, 5], 1), 5)
    ]

    for i, (result, expected) in enumerate(tests):
        if result != expected:
            raise ListDivideException(f"Test {i+1} failed")


test_list_divide()