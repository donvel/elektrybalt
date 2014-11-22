import math

from collections import defaultdict


MIN_PROB = 0.01


class Graph:
    def __init__(self, words):
        self.words = list(words)
        self.edges = defaultdict(int)
        self.probs = defaultdict(lambda: math.log(MIN_PROB / 10))
        self.degs = defaultdict(int)
        self.after = defaultdict(set)
        self.before = defaultdict(set)

    def add_edge(self, u, v):
        self.edges[u,v] += 1
        self.degs[u] += 1
        self.before[v].add(u)
        self.after[u].add(v)

   
    def count_probs(self):
        for ((u, v), val) in self.edges.items():
            self.probs[(u, v)] = math.log(
                    max(MIN_PROB, (val / self.degs[u]))
                    )

    

def from_file(words):
    g = Graph(set(words))
    for word, nxt in zip(words, words[1:]):
        g.add_edge(word, nxt)
    g.count_probs()
    for ((u,v), val) in g.edges.items():
        if val > 5:
            print(u, v, g.probs[u, v], g.degs[u])
    return g

