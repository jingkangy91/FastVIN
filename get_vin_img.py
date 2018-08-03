import pandas as pd
import requests
from bs4 import BeautifulSoup

filename = 'vin_list.csv'
df = pd.read_csv(filename)
df.drop(df.index[-5:], inplace=True)

# base_url = "http://application.vidc.info"
# post_url = base_url + "/subpage/nonloginprint.aspx"

begin_url = "http://application.vidc.info/Scripts/ImageHandler.ashx?vin="
end_url = "&sess=no&type=download/Certificate.png"

# for index, row in df.iterrows():
for index, row in df[:1].iterrows():
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
    # print(data)
    # sess = requests.Session()
    # req = sess.post(post_url, headers=headers, data=payload)
    # req.encoding = 'utf-8'
    # html = req.text
    # print(html)
    # print(req.cookies.get_dict())

    req = requests.get(url, stream=True)
    with open('./img/cert.png', 'wb') as f:
        f.write(req.content)