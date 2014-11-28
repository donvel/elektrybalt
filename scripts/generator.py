from collections import defaultdict
from utils import syl_len

INFTY = 1000000000.0


def create_inside(left, right, wg, syl_count):
    dp = defaultdict(lambda: (-INFTY, 'def_dp'))
    best = defaultdict(lambda: (-INFTY, 'def_best'))
    dp[0, left] = (0, 'start_dp')
    best[0] = (0, left if left else 'start_best')
    for i in range(1, syl_count + 1):
        for w in wg.words:
            lw = syl_len(w)
            if i - lw < 0:
                continue
            for v in wg.before[w]: # in wg.words
                cres = dp[i - lw, v][0] + wg.probs[v, w]
                dp[i, w] = max(dp[i, w], (cres, v))
           
            best_before = best[i - lw][1]
            cres = best[i - lw][0] + wg.probs[best_before, w]
            dp[i, w] = max(dp[i, w], (cres, best_before))
            best[i] = max(best[i], (dp[i, w][0], w))
    res = []
    i = syl_count
    w = right
    #for (k, v) in best.items():
    #    print (k, v)
   # print(dp[i, w][0])
    while i > 0:
        print(i, w, dp[i, w])
        res += [w]
        nw = dp[i, w][1]
        if wg.probs[nw, w] == wg.probs['kokoak', 'lolol']:
            print('XXXX')
        i -= syl_len(w)
        w = nw
    print()
    return list(reversed(res))


def first_upper(word):
    return word[0].upper() + word[1:]


def create_poem(word_graph, rhymes, syl_count, length):
    poem = []
    last_words = []
    for i in range(length):
        u, v = rhymes.random_rhyme()
        last_words += [u, v]
    left_word = None
    for right_word in last_words:
        inside = create_inside(left_word, right_word, word_graph, syl_count)
        left_word = right_word
        inside[0] = first_upper(inside[0])
        poem += [' '.join(inside)]
    for l in poem:
        print(l)
    return poem
