import re

VOWELS = set(
        ['a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę']
        )

def get_words(line):
    return [w.lower() for w in re.split('\W|\d|_', line, flags=re.U) if w]

def syl_len(word):
    return len([c for c in word if c in VOWELS])
