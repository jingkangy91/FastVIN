import pandas as pd
import os
import subprocess
import namereading

os.makedirs('pdf', exist_ok=True)

# list_name = input(
#     "Please input VIN list filename in 'list' dir (default 'vin_list.csv'):\n"
# )
# if list_name == '':
#     # list_name = 'vin_list.csv'
#     list_name = 'vin_list_test.csv'
# df = pd.read_csv(os.path.join('list', list_name))
# df.dropna(inplace=True)

df = namereading.read_name()

for index, row in df.iterrows():
    print("---------" + row['VIN'] + "----------")
    img_name = "Cert_" + row['VIN'] + ".png"
    pdf_name = "Cert_" + row['VIN'] + ".pdf"

    if pdf_name in os.listdir('pdf'):
        print(pdf_name + " already exists.")
    else:
        cmd = ['convert', 'img/'+ img_name, 'pdf/' + pdf_name]
        subprocess.call(cmd)
        print(pdf_name + " has been created.")