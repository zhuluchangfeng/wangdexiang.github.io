#import time
from functools import *
import pdfplumber
def extract_content(inputpath):
    """
    pdf文本抽取，储存在当前文件夹
    :param inputpath: pdf路径
    """
    path_pdf = inputpath
    path_text = path_pdf[:-3]+'txt'
    with pdfplumber.open(path_pdf) as pdf_file:
        l_page = map(lambda self: self.extract_text(), pdf_file.pages)

        context = reduce(lambda a, b: a+'\n'+b, l_page)

        with open(path_text, "w", encoding="utf-8") as file:
            file.write(context)