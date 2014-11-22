import argparse
import graph
import codecs
import utils
import rhymes
import generator


def get_args():
    parser = argparse.ArgumentParser(description="Generate a nice poem :)")
    
    parser.add_argument('--source_text', default='data/PanTadeusz.txt')
    parser.add_argument('--syllable_count', type=int, default=13)
    parser.add_argument('--rhyme_span', type=int, default=2)
    parser.add_argument('--length', type=int, default=4)
# parser.add_argument('--rhyme_pattern')
# parser.add_argument('--keyword_file')
# parser.add_argument('--markov_order')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    words = []
    with codecs.open(args.source_text, 'rb', encoding='utf8') as f:
        for l in f:
            words += utils.get_words(l.rstrip())
    wg = graph.from_file(words)
    rhs = rhymes.from_file(words, args.rhyme_span)
    poem = generator.create_poem(wg, rhs, args.syllable_count, args.length)
    
