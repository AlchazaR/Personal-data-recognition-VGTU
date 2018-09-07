

import string
# https://python-docx.readthedocs.io/en/latest/user/documents.html
# pip install python-docx
import docx
import pandas as pd


def read_file_content(fPath, fExt):
	fExt = fExt.lower()
	if fExt == '.txt':
		fText = read_txt(fPath)
	elif fExt == '.doc':
		fText = read_doc(fPath)
	elif (fExt == '.docx'):
		fText = read_docx(fPath)
	elif (fExt == '.xlsx'):
		fText = read_xls(fPath)
	elif (fExt == '.xls'):
		fText = read_xls(fPath)
	else: 
		fText = show_error(fPath)
	return(fText)

def read_txt(fPath):
	print("TXT - " + fPath)
	with open(fPath, 'r') as fh:
		content = fh.read()
	fText = Text(content)
	fh.close
	return(fText)

def read_doc(fPath):
	print("DOC - " + fPath)

def read_docx(fPath):
	print("DOCX - " + fPath)
	doc = docx.Document(fPath)
	fText = []
	for para in doc.paragraphs:
		fText.append(para.text)
	return(fText)

def read_xls(fPath):
	print("XLS - " + fPath)
	doc = pd.ExcelFile(fPath)
	df = pd.read_excel(fPath, sheet_name=None)
	dict(df)
	df = str(df)
	return(df)
	
def read_pdf(fPath):
	print("PDF - " + fPath)

def show_error(fPath):
	print("Unknown extension of file: ")

if __name__ == '__main__':
	print(read_file_content("C:\\Docs\\temp\\v9.xls", ".xls"))
    #read_file_content('/home/vlad/Documents/Repo/python_string-search/text_sources/Docker_Referatas.docx', '.docx')
