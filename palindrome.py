from utils import test

def isPalindrome(n):
    n = "".join(char for char in str(n) if char.isalnum()).lower().strip()
    for index in range(len(n)):
        if n[index] != n[-index-1]:
            return False
    return True

tests = {
    "racecar": True,
    1234: False,
    "bunny": False,
    1551: True,
    "kayak": True,
    "python": False,
    9889: True,
    "Madam": True,
    "Noon": True,
    "Hello": False,
    "A man, a plan, a canal: Panama": True,
    "Was it a car or a cat I saw?": True,
    "No 'x' in Nixon": True,
    "Not a palindrome!": False,
    12.21: True,
    45.54: True,
    1.23: False,
    "": True,
    "a": True,
    7: True,
    "   ": True
}

test(tests, isPalindrome)
