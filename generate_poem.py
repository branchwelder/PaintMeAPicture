""" Generates a poem from a string.
"""

from Rhymelessmaster.rhymeless import Rhymeless


poem_generator = Rhymeless()
book = open("Rhymelessmaster/books/otoos11.txt", "r")
lines = []
for line in book:
    lines.append(line)
book = "".join(lines)
# the book variable is just a huge string. I could also train
# on individual strings, or tweets, or virtually any other
# plain text content.

poem_generator.train(book)

if __name__ == '__main__':
    print poem_generator.generate_poem()
