import string
import os

def find_names():
    sourcePath = '/home/vlad/Documents/Mokslai/Baigiamasis darbas/wiki-straipsnis_vardai.txt'
    resultPath = '/home/vlad/Documents/Mokslai/Baigiamasis darbas/poliglot-result.txt'
    with open(sourcePath, 'r', encoding="utf16", errors='ignore') as fh:
        lines = fh.readlines()
    fh.close
    foundWords = 0
    for line in lines:
        print("Looking for line " + line)
        if line in open(resultPath, 'r').read():
            print(line + "found")
            foundWords = foundWords + 1
    print("Found " + str(foundWords) + " words")


def find(substr, infile, outfile):
  with open(infile) as a, open(outfile, 'w') as b:
   for line in a:
    if substr in line:
     b.write(line + '\n')


if __name__ == '__main__':
    #find_names()
    sourcePath = '/home/vlad/Documents/Mokslai/Baigiamasis darbas/wiki-straipsnis_vardai.txt'
    with open(sourcePath, 'r', encoding="utf16", errors='ignore') as fh:
        lines = fh.readlines()
    find('test string', 'a.txt', 'b.txt')

         