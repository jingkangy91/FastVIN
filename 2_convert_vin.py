#!/anaconda3/bin/python
import os
import pandas as pd
import PyPDF2
import subprocess
import namereading

os.makedirs('pdf', exist_ok=True)

df, list_name = namereading.read_name()

merger = PyPDF2.PdfFileMerger()
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
    
    merger.append('pdf/' + pdf_name)

output_name = list_name[:-3] + 'pdf'
merger.write(output_name)

print_or_not = input("Do you want to print it? (Y or Yes to print)\n")
if print_or_not.lower() == 'y' or 'yes':
    cmd = ['lpr', output_name]
    subprocess.call(cmd)