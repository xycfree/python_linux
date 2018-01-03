

from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from bs4 import BeautifulSoup

def convert_pdf_2_text(path):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()

    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    device1 = HTMLConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device1)

    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()
        with open('text.html', 'wb') as f:
            f.write(text)
        f.close()

    device.close()
    device1.close()
    retstr.close()

    return text
result = convert_pdf_2_text('qpl.PDF')
print(result)

# text = BeautifulSoup(result, 'lxml').text
# print(text)

