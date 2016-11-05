#!/usr/bin/env python
import os, sys

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag

# config
os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    execfile('settings.py')

DEFAULT_TAG = "holyoke"

def upload_files(filename):
    print("--- Uploading...")
    response = upload(filename)
    url = cloudinary_url(response['public_id'])
    return url

# upload_files("images/loading.png")

def cleanup():
    response = resources_by_tag(DEFAULT_TAG)
    count = len(response.get('resources', []))
    if (count == 0):
        print("No images found")
        return
    print("Deleting %d images..." % (count,))
    delete_resources_by_tag(DEFAULT_TAG)
    print("Done!")
    pass
