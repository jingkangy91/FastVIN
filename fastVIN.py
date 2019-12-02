#!/usr/bin/env python

import os
import pandas as pd
import requests
from PIL import Image
from bs4 import BeautifulSoup

def read_name():
    vin_name = input(
        "Please input VIN list filename in 'vin' dir " +
        "(default 'vin_list.csv'):\n"
    )
    if vin_name == '':
        vin_name = 'vin_list.csv'
        # vin_name = 'vin_list_test.csv'
    df = pd.read_csv(os.path.join('vin', vin_name))
    df.dropna(inplace=True)

    return df, vin_name

if not os.path.exists('vin') is True:
    print("Please check 'vin' folder.")

os.makedirs('img', exist_ok=True)
os.makedirs('pdf', exist_ok=True)

df, vin_name = read_name()
num_of_vins = len(df)

pdf_name = vin_name.split('.')[0] + '.pdf'

begin_url = "http://application.vidc.info/Scripts/ImageHandler.ashx?vin="
end_url = "&sess=no&type=download/Certificate.png"

img_list = []
for index, row in df.iterrows():
    print("[" + str(index + 1) + "/" + str(num_of_vins) + "]---------"
          + row['VIN'] + "----------")
    img_name = "Cert_" + row['VIN'] + ".png"

    if img_name in os.listdir('img'):
        print(img_name + " already exists.")
    else:
        url = begin_url + row['VIN'] + end_url
        headers = {
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/67.0.3396.99 Safari/537.36'
        }
        req = requests.get(url, stream=True)

        with open(os.path.join('img',img_name), 'wb') as f:
            f.write(req.content)
        print(img_name + " has been downloaded.")

    image = Image.open(os.path.join('img',img_name))
    im = image.convert('RGB')
    # print(index)
    if index == 0:
        im0 = im
    else:
        img_list.append(im)

print("Try to convert images to a pdf file.")
im0.save(os.path.join('pdf',pdf_name), save_all=True, append_images=img_list)
print("Done.")
