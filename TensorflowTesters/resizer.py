#Please change path and dimension tuple in im.resize to your needs
#

from PIL import Image
import os, sys

path = "/home/dhruv/Desktop/boxcut/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,360), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()
