from PyPDF2 import PdfMerger, PdfReader
import os

os.chdir('./pdf')

merger = PdfMerger()

for item in os.listdir():
    if item.endswith('.pdf'):
        merger.append(PdfReader(item))

merger.write('result.pdf')
