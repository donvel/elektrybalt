import math
import sys

from collections import defaultdict
from utils import normalize


MIN_PROB = 0.1
PENALTY = 0.01

class Graph:
    def __init__(self, words, length):
        self.words = list(words)
        self.edges = defaultdict(int)
        self.probs = defaultdict(lambda: math.log(PENALTY ** length))
        self.degs = defaultdict(int)
        self.after = defaultdict(set)
        self.before = defaultdict(set)
        self.length = length

    def add_edge(self, u, v):
        self.edges[u,v] += 1
        self.degs[u,len(u)] += 1
        self.before[v].add(u)
        self.after[u].add(v)

   
    def count_probs(self):

        for w in self.words:
            self.add_edge((), w)

        for ((u, v), val) in self.edges.items():
            penalty = PENALTY ** (self.length - len(u))
            self.probs[(u, v)] = math.log(
                    # max(MIN_PROB, (val / self.degs[u]))
                    penalty * max(MIN_PROB, (val / self.degs[u,len(u)]))
                    )

    

def from_file(words, length):
    g = Graph(set(normalize(w) for w in words), length)
    for i in range(len(words)):
        w = normalize(words[i])
        prev = tuple(normalize(p) for p in words[max(0,i-length):i])
        for j in range(len(prev) + 1):
            if not any(p[-1] == '.' for p in prev[j:]):
                g.add_edge(prev[j:], w)
            #g.add_edge(prev[-1], w)
    g.count_probs()
    for ((u,v), val) in g.edges.items():
        if (len(u) >= 1 and val > 5) or (len(u) >= 2 and val > 1):
            print(u, v, g.probs[u, v], g.degs[u, len(u)], file=sys.stderr)
    return g

