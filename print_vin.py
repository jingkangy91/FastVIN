import PyPDF2, os
import pandas as pd
import subprocess

list_name = input(
    "Please input VIN list filename in 'list' dir (default 'vin_list.csv'):\n"
)
if list_name == '':
    # list_name = 'vin_list.csv'
    list_name = 'vin_list_test.csv'
df = pd.read_csv(os.path.join('list', list_name))
df.dropna(inplace=True)

merger = PyPDF2.PdfFileMerger()
for index, row in df.iterrows():
    print("---------" + row['VIN'] + "----------")
    # img_name = "Cert_" + row['VIN'] + ".png"
    pdf_name = "Cert_" + row['VIN'] + ".pdf"

    # with open(os.path.join('pdf', pdf_name), 'rb') as f:
        # merger.append(f)
    merger.append('pdf/'+pdf_name)
    
# with open('vin_list.pdf', 'wb') as f:
#     merger.write(f)

output_name = list_name[:-3] + 'pdf'
merger.write(output_name)

    # if pdf_name in os.listdir('pdf'):
    #     print(pdf_name + " already exists.")
    # else:
    #     cmd = ['convert', 'img/'+ img_name, 'pdf/' + pdf_name]
    #     subprocess.call(cmd)
    #     print(pdf_name + " has been created.")

cmd = ['lpr', output_name]
subprocess.call(cmd)