from utils import test

def freq_check(nums: list, x: int, y: int) -> bool:
    freq_x = 0
    for num in nums:
        if num == x:
            freq_x += 1
    if freq_x >= y:
        return True
    return False

tests = {
    ((1, 2, 2, 3), 2, 2): True,
    ((1, 2, 2, 3), 2, 3): False,
    ((5, 5, 5, 5), 5, 4): True,
    ((5, 5, 5, 5), 5, 5): False,
    ((1, 2, 3), 4, 1): False,
    ((1, 1, 1, 2, 2), 1, 3): True,
    ((1, 1, 1, 2, 2), 2, 2): True,
    ((1, 1, 1, 2, 2), 2, 3): False,
    ((), 1, 1): False,
    ((0, 0, 0), 0, 2): True,
}

test(tests, lambda args: freq_check(*args))