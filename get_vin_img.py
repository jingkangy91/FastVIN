import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import subprocess

list_name = input(
    "Please input VIN list filename in 'list' dir (default 'vin_list.csv'):\n"
)
if list_name == '':
    list_name = 'vin_list.csv'
df = pd.read_csv(os.path.join('list', list_name))
df.dropna(inplace=True)

begin_url = "http://application.vidc.info/Scripts/ImageHandler.ashx?vin="
end_url = "&sess=no&type=download/Certificate.png"

for index, row in df.iterrows():
# for index, row in df[:300].iterrows():
    print("---------" + row['VIN'] + "----------")
    img_name = "Cert_" + row['VIN'] + ".png"
    pdf_name = "Cert_" + row['VIN'] + ".pdf"

    # Check is exist or not
    if img_name in os.listdir('img'):
        print(img_name + " already exists.")
    else:
        url = begin_url + row['VIN'] + end_url

        # payload = {
        #     'TextBox_vin': row['VIN'],
        #     'TextBox_jkzms': row['Import Certificate Number'],
        # }
        headers = {
            'user-agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/67.0.3396.99 Safari/537.36'
        }
        req = requests.get(url, stream=True)

        with open('img/' + img_name, 'wb') as f:
            f.write(req.content)
        print(img_name + " has been downloaded.")

    if pdf_name in os.listdir('pdf'):
        print(pdf_name + " already exists.")
    else:
        cmd = ['convert', 'img/' + img_name, 'pdf/' + pdf_name]
        subprocess.call(cmd)
        print(pdf_name + " has been created.")