import re

VOWELS = set(
        ['a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę']
        )

def get_words(line):
    return [w for w in re.split(r'\s|\d|[^\w,.]', line) if any(c.isalpha() for c in w)]

def normalize(word):
    w = word.lower()
    if w[-1] in ['.', ',']:
        w = w[:-1]
    return w

def syl_len(word):
    return len([c for c in word if c in VOWELS])
