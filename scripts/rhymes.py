from collections import defaultdict
from utils import VOWELS, normalize
import random

def is_vowel(char):
    return char in VOWELS


def get_end(word, span):
    i = len(word)
    cnt = 0
    while True:
        i -= 1
        if is_vowel(word[i]):
            cnt += 1
        if i == 0 or cnt == span:
            break

    return word[i:]

class Rhymes:
    def __init__(self, words, span):
        self.words = list(words)
        self.rhymes = defaultdict(set)
        for w in self.words:
            end = get_end(normalize(w), span)
            self.rhymes[end].add(w)
        self.rhymes = [list(l) for (k, l) in self.rhymes.items() if len(l) > 1]

    def random_rhyme(self):
        choices = random.choice(self.rhymes)[:]
        random.shuffle(choices)
        return (choices[0], choices[1])



def from_file(words, span):
    rhs = Rhymes(words, span)
    for v in rhs.rhymes:
        if len(v) > 5:
            print(v)
    return rhs
