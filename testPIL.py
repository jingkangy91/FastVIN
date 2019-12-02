#!/usr/bin/env python

from PIL import Image

image1 = Image.open('img/Cert_5YJSA7E20JF255212.png')
im1 = image1.convert('RGB')
im1.save('Cert_5YJSA7E20JF255212.pdf')
