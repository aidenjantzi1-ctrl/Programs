from utils import test

def remove_duplicates(nums: list) -> list:
    unique_list = []
    for num in nums:
        if not num in unique_list:
            unique_list.append(num)
    return unique_list

tests = {
    (): [],
    (1,): [1],
    (1, 2, 2, 4, 3): [1, 2, 4, 3],
    (5, 5, 5, 5): [5],
    (1, 2, 3, 4): [1, 2, 3, 4],
    (3, 2, 3, 1, 2): [3, 2, 1],
    (-1, -1, 0, 1, 0): [-1, 0, 1],
}

test(tests, remove_duplicates)