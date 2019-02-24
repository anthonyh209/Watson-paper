import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions, ConceptsOptions, RelationsOptions
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def analysisTop(information):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='p196zY7-l6kkM3G1pKfXjtDFhFGzicxZFIsYEraMXSq7',
        url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
    )

    response = natural_language_understanding.analyze(text=information,
                                                      features=Features(
                                                          relations=RelationsOptions())).get_result()

    print(json.dumps(response, indent=2))





# response = natural_language_understanding.analyze(
#     url='www.cnn.com',
#     features=Features(categories=CategoriesOptions(limit=3))).get_result()
#
# print(json.dumps(response, indent=2))

    # response = natural_language_understanding.analyze(
    #     url='www.eurosport.com',
    #     features=Features(concepts=ConceptsOptions(limit=10))).get_result()

    #response = natural_language_understanding.analyze(
    #    text=information,
    #    features=Features(concepts=ConceptsOptions(limit=10))).get_result()




#print(json.dumps(response, indent=2))


pdfDir = "/Users/anthony/desktop/test/"
for pdf in os.listdir(pdfDir):
    first = pdf


fileExtension = first.split(".")[-1]
if fileExtension == "pdf":
    pdfFilename = pdfDir + first
    text = convert(pdfFilename) #get string of text content of pdf
    #print(text)
    analysisTop(text)

    #textFilename = txtDir + pdf + ".txt"
    #textFile = open(textFilename, "w") #make text file
    #textFile.write(text) #write text to text file






