import time
import sys
import string

import file_scanner
import file_reader

""" Horspool string search algorithm """
# preprocess - initialize occ
def preprocess(pattern):
    #print(pattern)
    occ = dict.fromkeys(string.ascii_lowercase, -1)
    for i in range(0,len(pattern)-1):
        occ[pattern[i]] = i
    return occ

# seach - find string with horspool
def horspool_search(text,pattern,occ):
    found = 0
    i = 0
    m = len(pattern)
    n = len(text)

    while i <= n-m:
        j = m-1
        while j >= 0 and pattern[j] == text[i+j]:
            j = j-1
        if j < 0:
            found = found+1
            #print("found!")
        i = i + m-1
        #text.replace('\n', '')
        #print('OCC - ' + str(occ[text[i]]) + ' OCC! ') 
        try:
            i = i - occ[text[i]]
        except KeyError:
            err = 1
    return found

""" Knutt-Morris-Pratt """
def kmp_search(text, pattern):
    d = {0:0}
    template = pattern + '#' + text
    for i in range(1,len(template)):
        j = d[i-1]
        while j > 0 and template[j] != template[i]:
            j = d[j-1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(pattern):
            return i
    return None 


### TEST FUNCTION ###

if __name__ == '__main__':

	# get files using file_scanner
    files = file_scanner.get_files('/home/vlad/Documents/Repo/python_string-search/text_sources/')
    for i in range(6, 7):
        print(str(i) + '. Horspool')
        for found_file in files:
            #def show_match(text, pattern):
            #print ('Text:  %s' % text)
            fh = open('/home/vlad/Documents/Repo/python_string-search/text_sources/vardai-pavardes.txt', 'r', encoding="utf8")
            foundNamesCount = 0
            fContent = file_reader.read_file_content(found_file[0], found_file[2])
            fContent.replace('\n', ' ')
            start_time = time.time()
            for line in fh:
                line.replace('\n', '')
                pattern = ''.join(line)
                pattern.replace('\n', '')
                occ = preprocess(pattern)
                #print("Searching for " + pattern + " in file " + found_file[0]) 
                results = horspool_search(fContent, pattern, occ)
            #print ('Match: %s%s' % (*p, pattern))
            print('### Found ' + str(foundNamesCount) + ' names in file ' + found_file[0] + '. Took ' + str(time.time() - start_time))
            fh.close
			
    
    """for i in range(1, 7):
        print(str(i) + '. Knutt Moris Pratt')
        for found_file in files:
            fh = open('/home/vlad/Documents/Repo/python_string-search/text_sources/vardai-pavardes.txt', 'r', encoding="utf8")
            foundNamesCount = 0
            fContent = file_reader.read_file_content(found_file[0], found_file[2])
            fContent.replace('\n', ' ')
            start_time = time.time()
            for line in fh:
                pattern = ''.join(line)
                results = kmp_search(fContent, pattern)
                if results != None:
                    foundNamesCount += 1
            print('### Found ' + str(foundNamesCount) + ' names in file ' + found_file[0] + '. Took ' + str(time.time() - start_time))
            fh.close"""