

def read_file_content(fPath, fExt):
    fExt = fExt.lower()
    if fExt == '.txt':
        read_txt(fPath)
    elif fExt == '.doc':
        read_doc(fPath)
    elif fExt == '.docx':
        read_docx(fPath)

def read_txt(fPath):
    print("TXT - " + fPath)

def read_doc(fPath):
    print("DOC - " + fPath)

def read_docx(fPath):
    print("DOCX - " + fPath)

def read_xls():
    print("XLS - " + fPath)

def read_xlsx():
    print("XLSX - " + fPath)

def read_pdf():
    print("PDF - " + fPath)

def show_error():
    print("Unknown extension of file: ")

if __name__ == '__main__':
    read_file_content('/home/vlad/Documents/Repo/python_string-search/text_sources/Docker_Referatas.docx', '.docx')
