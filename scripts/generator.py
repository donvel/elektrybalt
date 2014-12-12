import sys
from collections import defaultdict
from utils import syl_len

INFTY = 1000000000.0

"""
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
"""


def join_pre(pre, w, l):
    return tuple((list(pre) + [w])[l:])

def fill_poem(fixed, forb, wg, syl_count, length):
    l = syl_count * length
    dp = defaultdict(lambda: (-INFTY, (), 'default_dp'))
    dp[0, ()] = (0, (), 'start_dp')
    
    for i in range(1, l + 1):
        
        word_choice = wg.words if i not in fixed else [fixed[i]]
        
        #if i in fixed:
        #    print("Fixed word: {}".format(word_choice[0]))


        for w in word_choice:
            lw = syl_len(w)
            #if i - lw == 0:
            #    print(w)
            
            if i not in fixed:
                crash = False
                for j in range(i - lw + 1, i + 1):
                    if j in forb:
                        crash = True
                        break
                if crash:
                    #print("Crash!")
                    continue
                #print("No crash!")

            for pre in wg.before[w]: # in wg.words
                #if i in fixed:
                #    print("pre: {}".format(pre))
                cres = dp[i - lw, pre][0] + wg.probs[pre, w]
                
                #if i - lw == 0 and len(pre) == 0:
                #    print(pre, w)
                #if cres > -INFTY:
                #    print("cres = {}".format(cres))
                for pi in range(len(pre) + 2):
                    new_pre = join_pre(pre, w, pi)
                    dp[i, new_pre] = max(dp[i, new_pre], (cres, pre, w))
                    #if cres > -INFTY:
                    #    print("dp[{},{}] = {}".format(i, new_pre, dp[i, new_pre]))
           
    lres = []
    res = []
    i = l
    pre = ()
    w = None

    while i > 0:
        print(i, pre, dp[i, pre], wg.edges[pre, w], file=sys.stderr)#, wg.edges[pre, w], wg.degs[pre, len(pre)])
        
        #if wg.probs[pre, w] == wg.probs['kokoak', 'lolol']:
        #    print('XXXX')
        w = dp[i, pre][2]
        lres += [w]
        
        
        pre = dp[i, pre][1]
        i -= syl_len(w)
        
        if i % syl_count == 0:
            res += [list(reversed(lres))]
            lres = []
    print(file=sys.stderr)
    return list(reversed(res))


def first_upper(word):
    return word[0].upper() + word[1:]


def place_words(last_words, syl_count):
    places = {}
    forb = {}
    it = syl_count
    forb[0] = True
    for w in last_words:
        places[it] = w
        for j in range(it + 1 - syl_len(w), it + 1):
            forb[j] = True
        it += syl_count
    print(sorted(list(places.items())), sorted(list(forb)), file=sys.stderr)
    return places, forb


def create_poem(word_graph, rhymes, syl_count, length):
    poem = []
    last_words = []
    for i in range(length):
        u, v = rhymes.random_rhyme()
        last_words += [u, v]
    fixed, forb = place_words(last_words, syl_count)
    lines = fill_poem(fixed, forb, word_graph, syl_count, 2 * length)
    """left_word = None
    for right_word in last_words:
        inside = create_inside(left_word, right_word, word_graph, syl_count)
        left_word = right_word
    """
    poem = []
    for l in lines:
        l[0] = first_upper(l[0])
        poem += [' '.join(l)]
    for l in poem:
        print(l)
    return poem
