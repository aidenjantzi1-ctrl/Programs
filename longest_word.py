from utils import test


def find_longest_word(txt_in: str) -> str:
    values = []
    for i in txt_in.splitlines():
        if not isinstance(i, int):
            values.append(i)
    longest = ""
    for word in values:
        if len(word) > len(longest):
            longest = word
    return longest


def find_longest_word_input():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)


tests = {
    """3
Banana
Grape
Watermelon""": "Watermelon",
    """4
apple
banana
kiwi
grape""": "banana",
    """5
hello
cat
world
python
code""": "python",
    """2
a
ab""": "ab",
    """3
sun
moon
star""": "moon",
}

test(tests, find_longest_word)
