""" Gets images from Getty Images based on searchterm.

    Dependencies: pycurl (for ubuntu: sudo apt install python-pycurl)
"""

# import all those packages
import json
import pycurl
from StringIO import StringIO
import urllib
import cStringIO
from PIL import Image

def imager(searchterm_list):
    """ Saves images from the searchterms into Collagerator/images.

        Takes in: list of searchterms
        Returns: list of images (i.e., ['images/loading.png', 'images/searchterm.jpg'])
        Saves images in PaintMeAPicture/Collagerator/images
    """
    file_loc_list = []
    for term in searchterm_list:
        get_image(term)
        file_loc_list.append('images/' + term + '.jpg')
    return file_loc_list


def get_image(searchterm):
    """ Gets an image from Getty Images API and saves it.
    """
    # retrieve image from Getty Images API
    buf = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, "https://api.gettyimages.com/v3/search/images?phrase=" + searchterm)
    c.setopt(c.HTTPHEADER, ['Api-Key:' + 'mu5xa4dbfaj6ucbb4xr85ka3']) # credentials['gettykey']])
    c.setopt(c.WRITEDATA, buf)
    c.perform()
    # get uri and save it to that Collagerator/images
    dictionary = json.loads(buf.getvalue())
    img_uri = dictionary[u'images'][0][u'display_sizes'][0][u'uri']
    image = save_image(img_uri, searchterm)


def save_image(url, searchterm):
    """ Opens the image url and save it into the
        PaintMeAPicture/Collagerator/images folder.
    """
    file = cStringIO.StringIO(urllib.urlopen(url).read())
    img = Image.open(file)
    img.save('Collagerator/images/' + searchterm + '.jpg')


if __name__ == '__main__':
    imager(['computer','dog'])
