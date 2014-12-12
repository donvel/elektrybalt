from collections import defaultdict
from utils import is_vowel, RULES, normalize
import random
import sys



def get_end(word, span):
    i = len(word)
    cnt = 0
    while True:
        i -= 1
        if is_vowel(word[i]) and not any(r(word, i) for r in RULES):
            cnt += 1
        if i == 0 or cnt == span:
            break

    return word[i:]


def rhymes_with(c1, c2, span):
    w1 = normalize(c1)
    w2 = normalize(c2)
    if len(w1) < 3 or len(w2) < 3:
        return False
    if w1 in w2 or w2 in w1:
        return False
    return get_end(w1, span) == get_end(w2, span)
      


class Rhymes:
    def __init__(self, words, span):
        self.words = list(words)
        self.span = span
        """
        self.rhymes = defaultdict(set)
        for w in self.words:
            #if w[-1] in ('.', ','):
            end = get_end(normalize(w), span)
            self.rhymes[end].add(w)
        self.rhymes = [list(l) for (k, l) in self.rhymes.items() if len(l) > 1]
        """

    def random_rhyme(self):
        c1 = 'a'
        c2 = 'a'
        while not rhymes_with(c1, c2, self.span):
            c1 = normalize(random.choice(self.words))
            c2 = normalize(random.choice(self.words))
        return (c1, c2)



def from_file(words, span):
    rhs = Rhymes(words, span)
    return rhs
    """for v in rhs.rhymes:
        if len(v) > 5:
            print(v)
    return rhs"""
