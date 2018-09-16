import string
# https://python-docx.readthedocs.io/en/latest/user/documents.html
# pip install python-docx
import docx
import pandas as pd
import PyPDF2
# install apps before install textract - apt-get install swig 
# apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev
# apt-get install libpulse-dev
import textract 


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
	elif (fExt == '.pdf'):
		fText = read_pdf(fPath)
	else: 
		fText = show_error(fPath)
	return(fText)

	
def read_txt(fPath):
	print("TXT - " + fPath)
	with open(fPath, 'r') as fh:
		content = fh.read()
	#fText = Text(content)
	fText = content
	fh.close
	return(fText)

	
def read_doc(fPath):
	return("DOC - " + fPath)
	"""
		https://stackoverflow.com/questions/16516044/is-it-possible-to-read-word-files-doc-docx-in-python
		Yes it is possible. LibreOffice (at least) has a command line option to convert files that works a treat. Use that to convert the file to text. 
		Then load the text file into Python as per routine manoeuvres.
		This worked for me on LibreOffice 4.2 / Linux:
		soffice --headless --convert-to txt:Text /path_to/document_to_convert.doc
		I've tried a few methods (including odt2txt, antiword, zipfile, lpod, uno). 
		The above soffice command was the first that worked simply and without error. 
		This question (http://ask.libreoffice.org/en/question/14130/how-do-i-install-filters-for-the-soffice-command/) on using filters 
		with soffice on ask.libreoffice.org (http://ask.libreoffice.org/en/question/14130) helped me.
	"""

	
def read_docx(fPath):
	print("DOCX - " + fPath)
	doc = docx.Document(fPath)
	fText = []
	for para in doc.paragraphs:
		fText.append(para.text)
	return(fText)

	
def read_xls(fPath):
	print("XLS - " + fPath)
	#doc = pd.ExcelFile(fPath)
	df = pd.read_excel(fPath, sheet_name=None)
	dict(df)
	df = str(df)
	return(df)
	
	
def read_pdf(fPath):
	print("PDF - " + fPath)
	# If it's scanned file, PyPDF2 will not find any words in it
	# In this case OCR is needed
	"""if fText != "":
		fText = fText
	else:
		fText = textract.process(fPath, method='tesseract', language='eng')"""
	try:
		fText = textract.process(fPath, encoding = 'utf-8') #encoding = 'unicode_escape')
	except UnicodeDecodeError:
		return('File', fPath, 'cannot be extracted! - skipped')
	return(fText)

	
def show_error(fPath):
	return("Unknown extension of file: ")

	
if __name__ == '__main__':
	#print(read_file_content("C:\\Docs\\temp\\test.pdf", ".pdf"))

	#print(read_file_content("C:\\Docs\\temp\\v9.xls", ".xls"))
    print(read_file_content('/home/vlad/Documents/Repo/python_string-search/text_sources/Referatas.pdf', '.pdf'))