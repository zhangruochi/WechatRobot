# -*- coding: utf-8 -*-"
import os
from cStringIO import StringIO
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import argparse

def convert_pdf_2_text(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text


def wrire_text(text, output_file):
    with open(output_file, mode="w") as f:
        f.write(text)


def main(file):
    if not os.path.exists("output.txt"):
        file = open("output.txt", 'w')
        

    try:
        text = convert_pdf_2_text(pdf_file)
    except:
        text = "error"   
    
    wrire_text(text, "output.txt")


if __name__ == '__main__':
    """
    path = "docs.pdf"
    text = convert_pdf_2_text(path)
    print text
    save_txt(text,path)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    pdf_file = args.file
    main(pdf_file)