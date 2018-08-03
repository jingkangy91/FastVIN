import pandas as pd
import requests
from bs4 import BeautifulSoup

filename = 'vin_list.csv'
df = pd.read_csv(filename)
df.drop(df.index[-5:], inplace=True)

base_url = "http://application.vidc.info"
post_url = base_url + "/subpage/nonloginprint.aspx?"

# for index, row in df.iterrows():
for index, row in df[:1].iterrows():
    payload = {
        'TextBox_vin': row['VIN'],
        'TextBox_jkzms': row['Import Certificate Number'],
    }
    # print(data)
    req = requests.post(post_url, data=payload)
    req.encoding = 'utf-8'
    html = req.text
    print(html)
    # print(req.cookies.get_dict())