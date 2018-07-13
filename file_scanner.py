import glob, os
import sys
import platform
import hashlib


rootPath = r'C:\Docs\Mokslai\BD\prototipas\test dir'
searchExt = [".doc", ".docx", ".xls", ".xlsx", ".pdf", ".txt"]
os.chdir(rootPath)

class FileData:
    dfType = ''
    dfHash = ''
    
    def __init__(self, dfName):
        self.name = dfName
        """
        Get files MD5 hash
        Source - https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
        """
        blocksize=2**20
        m = hashlib.md5()
        with open( os.path.join(fPath) , "rb" ) as f:
            while True:
                buf = f.read(blocksize)
                if not buf:
                    break
                m.update( buf )
        self.dfHash = m.hexdigest()


def storeFile (fDir, fName):
    """
    Get file path and filename
    """
    return os.path.join(fDir, fName)

def getFileMetaData (fPath):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(fPath)
    else:
        stat = os.stat(fPath)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime



if __name__ == '__main__':
    for dirname, dirnames, filenames in os.walk(rootPath):
        # exclude these directories from search
        if 'Windows' in dirnames:
            dirnames.remove('Windows')
        if 'Program files' in dirnames:
            dirnames.remove('Program files')
        if 'Program files (x86)' in dirnames:
            dirnames.remove('Program Files (x86)')
        if 'App32' in dirnames:
            dirnames.remove('App32')
        if 'App64' in dirnames:
            dirnames.remove('App64')

        # print path to all found filenames and file hash
        for filename in filenames:
            if filename.endswith(tuple(searchExt)): 
                fPath = storeFile(dirname, filename)
                file = FileData(fPath)
                print (file.name, file.dfHash)
                
                
