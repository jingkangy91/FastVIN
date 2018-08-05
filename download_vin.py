import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

os.makedirs('img', exist_ok=True)

list_name = input(
    "Please input VIN list filename in 'list' dir (default 'vin_list.csv'):\n"
)
if list_name == '':
    # list_name = 'vin_list.csv'
    list_name = 'vin_list_test.csv'
df = pd.read_csv(os.path.join('list', list_name))
df.dropna(inplace=True)

begin_url = "http://application.vidc.info/Scripts/ImageHandler.ashx?vin="
end_url = "&sess=no&type=download/Certificate.png"

for index, row in df.iterrows():
    print("---------" + row['VIN'] + "----------")
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