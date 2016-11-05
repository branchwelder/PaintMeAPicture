""" Generates a poem from a string.
"""

from Rhymelessmaster.rhymeless import Rhymeless


keyword_dict = {'darwin': 'otoos11', 'evolution': 'otoos11',
    'war': 'wp', 'warren': 'wp',
    'carroll': 'wonderland',
    'shakespeare': 'shakespeare'}

def poetry(keyword):
    poem_generator = Rhymeless()
    if keyword.lower() in keyword_dict:
        book = open("Rhymelessmaster/books/" + keyword_dict[keyword] + '.txt', 'r')
    else:
        book = keyword
    lines = []
    for line in book:
        lines.append(line)
    book = "".join(lines)
    poem_generator.train(book)
    return poem_generator.generate_poem()

if __name__ == '__main__':
    print poetry('carroll')
