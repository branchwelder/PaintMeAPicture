""" Gets images from Getty Images from a sentence.

    Dependencies: pycurl (for ubuntu: sudo apt install python-pycurl)
                  pattern (for ubuntu: pip install pattern)
"""

# import all those packages
import json
import pycurl
from StringIO import StringIO
import urllib
import cStringIO
from PIL import Image
import random
from pattern.en import parse

def get_images_from_sentence(sentence):
    """ Takes in a sentence, saves the images to the correct directory, and
        returns a list of filepaths to the images.
    """
    nouns = remove_reserves(parser(sentence))
    return imager(nouns)


def imager(searchterm_list):
    """ Saves images from the searchterms into Collagerator/images.

        Takes in: list of searchterms
        Returns: list of images (i.e., ['images/loading.png', 'images/searchterm.jpg'])
        Saves images in PaintMeAPicture/Collagerator/images
    """
    file_loc_list = []
    for term in searchterm_list:
        if not term:
            new_term = random.choice(cat_terms)
        else:
            words = term.split()
            new_term = words[0]
            num_words = len(words)
            for i in range(1, num_words):
                new_term = new_term + '%20' + words[i]
        get_image(new_term)
        file_loc_list.append('Collagerator/images/' + new_term + '.jpg')
    return file_loc_list


def get_image(searchterm):
    """ Gets an image from Getty Images API and saves it.
    """
    # retrieve image from Getty Images API
    buf = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, "https://api.gettyimages.com/v3/search/images/creative?phrase=" + searchterm)
    c.setopt(c.HTTPHEADER, ['Api-Key:' + 'mu5xa4dbfaj6ucbb4xr85ka3']) # credentials['gettykey']])
    c.setopt(c.WRITEDATA, buf)
    c.perform()

    # get uri and save it to that Collagerator/images
    dictionary = json.loads(buf.getvalue())
    if len(dictionary[u'images']) == 0:
        get_image(random.choice(cat_terms))
    else:
        index = random.randint(0,len(dictionary))
        img_uri = dictionary[u'images'][index][u'display_sizes'][0][u'uri']
        image = save_image(img_uri, searchterm)
    # randomly choose an image from the dictionary


def save_image(url, searchterm):
    """ Opens the image url and save it into the
        PaintMeAPicture/Collagerator/images folder.
    """
    file = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(file)
    img.save('Collagerator/images/' + searchterm + '.jpg')


def parser(text):
    """ Takes in a sentence (string) and returns a list of nouns (strings).
    """
    list_parsed = parse(text).split()
    nouns = []
    for i in list_parsed[0]:
        if 'NN' in i[1]:
            nouns.append(str(i[0]))
    return nouns


def remove_reserves(list_nouns):
    """ Takes in a list of nouns (strings) and returns a list of nouns that are
        not reserved (strings).
    """
    for noun in list_nouns:
        if noun in reserve_words:
            list_nouns.remove(noun)
    return list_nouns


reserve_words = ['picture', 'painting', 'me', 'i']

cat_terms = ['cat', 'lion', 'tiger', 'liger', 'feline', 'large cat',
                'kitty', 'kitten', 'lynx', 'cat cat cat cat cat', 'kitty kat']

if __name__ == '__main__':
    # get_image('woman%20search')
    imager(['person walking', 'god'])
    # imager(['multiword search term'])
