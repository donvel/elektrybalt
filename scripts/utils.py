import re

def ivow(word, i):
    return i + 1 < len(word) and word[i] == 'i' and is_vowel(word[i + 1])

RULES = [ivow]

VOWELS = set(
        ['a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó']
        )

HYPHENS = set('-')

def is_vowel(char):
    return char in VOWELS

def clean_hyphens(w):
    res = [c for c in w if c not in HYPHENS]
    return ''.join(res)

def get_words(line):
    return [clean_hyphens(w) for w in re.split(r'\s|\d|[^\w,.-]', line) if any(c.isalpha() for c in w)]

def normalize(word):
    w = word.lower()
    while w[-1] in ['.', ',']:
        w = w[:-1]
    return w

def syl_len(word):
    return len([c for (i, c) in enumerate(word) if (c in VOWELS
        and not any(r(word, i) for r in RULES))])

