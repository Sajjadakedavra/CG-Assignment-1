# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:10:03 2020

@author: Sajjad
"""

from PIL import Image
from PIL.ExifTags import TAGS


def displayImgProps():
    imageName = r'E:\personal data e\All DSLR Pictures\5th dec. Bday\IMG_3400.jpg'
    image = Image.open(imageName)
    exifdata = image.getexif()
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")
        print("---------------------------------")
        
        

        
displayImgProps()