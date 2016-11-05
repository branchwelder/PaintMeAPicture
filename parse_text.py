""" Parses sentences and pulls out nouns.
"""

from pattern.en import parse

def parser(text):
    list_parsed = parse(text).split()
    nouns = []
    for i in list_parsed[0]:
        if 'NN' in i[1]:
            nouns.append(str(i[0]))
    return nouns

def remove_reserves(list_nouns):
    for noun in list_nouns:
        if noun in reserve_words:
            list_nouns.remove(noun)
    print list_nouns

reserve_words = ['picture', 'painting', 'me', 'i']

if __name__ == '__main__':
    remove_reserves(parser('draw me a picture of a cat'))
