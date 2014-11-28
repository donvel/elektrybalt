import re

def ivow(word, i):
    return i + 1 < len(word) and word[i] == 'i' and is_vowel(word[i + 1])

RULES = [ivow]

VOWELS = set(
        ['a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę']
        )

def is_vowel(char):
    return char in VOWELS

def get_words(line):
    return [normalize(w) for w in re.split(r'\s|\d|[^\w,.]', line) if any(c.isalpha() for c in w)]

def normalize(word):
    w = word.lower()
    if w[-1] in ['.', ',']:
        w = w[:-1]
    return w

def syl_len(word):
    return len([c for (i, c) in enumerate(word) if (c in VOWELS
        and not any(r(word, i) for r in RULES))])

