""" Generates a poem from a string.
"""

from Rhymelessmaster.rhymeless import Rhymeless


keyword_dict = {'darwin': 'otoos11', 'evolution': 'otoos11',
    'war': 'wp', 'warren': 'wp',
    'carroll': 'wonderland','alice':'wonderland',
    'shakespeare': 'shakespeare',
    'bee': 'beemovie',
    'plato':'republic',
    'don quixote':'996',
    'america':'18127',
    'odysseus':'ulysses',
    'draco':'myimmortal'}

def poetry(keyword):
    poem_generator = Rhymeless()
    if keyword.lower() in keyword_dict:
        book = open("Rhymelessmaster/books/" + keyword_dict[keyword] + '.txt', 'r')
        print 'opened book'
    else:
        book = keyword
    lines = []
    for line in book:
        lines.append(line)
    book = "".join(lines)
    book = "me"
    print 'formatted'
    poem_generator.train(book)
    print 'trained'
    print poem_generator.generate_poem()

if __name__ == '__main__':
    print poetry('copy')
