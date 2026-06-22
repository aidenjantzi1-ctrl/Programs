import utils

def isPrime(n: int):
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

tests = {
    2: True,
    3: True,
    4: False,
    5: True,
    11: True,
    15: False,
    23: True,
    29: True,
    30: False,
    97: True,
    100: False
}

utils.test(tests, isPrime)
