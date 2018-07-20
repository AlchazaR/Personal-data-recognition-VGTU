import time
import sys
import string
#import ahocorasick

""" Boyer Moore string search algorithm """
class last_occurrence(object):
    """Last occurrence functor."""

    def __init__(self, pattern, alphabet):
        """Generate a dictionary with the last occurrence of each alphabet
        letter inside the pattern.
        
        Note: This function uses str.rfind, which already is a pattern
        matching algorithm. There are more 'basic' ways to generate this
        dictionary."""
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        """Return last position of the specified letter inside the pattern.
        Return -1 if letter not found in pattern."""
        return self.occurrences[letter]

def boyer_moore_match(text, pattern):
    """Find occurrence of pattern in text."""
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1+l)
            j = m - 1 
    return -1


""" Horspool string search algorithm """
# preprocess - initialize occ
def preprocess(pattern):
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
            print("found!")
        i = i + m-1
        i = i - occ[text[i]]
    return found

""" Knutt-Morris-Pratt """
def kmp_search(text, pattern):
    d = {0:0}
    template = pattern + '#' + text
    for i in xrange(1,len(template)):
        j = d[i-1]
        while j > 0 and template[j] <> template[i]:
            j = d[j-1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(pattern):
            return i
    return None 

def string_search(text, pattern):
    i=j=0
    lengthS = len(text)
    lengthX = len(pattern)
    while i<=lengthS - lengthX and j>lengthX:
     
        if li[i+j]==x[j]:
            j+=1
        
        else:
            i+=1
            j=0
    
    return i if j==lengthX else None

if __name__ == '__main__':
    fh = open('text_sources/test-list.txt', 'r')     
    
    """ Boyer Moore algorithm test """
    start_time = time.time()
    for line in fh:
        pattern = ''.join(line)
        print("Looking for word - " + pattern)
        f = open('text_sources/wiki-straipsnis.txt', 'r')
        text=f.read()
        results = boyer_moore_match(text, pattern)
        print(results)
    print("Boyer More took --- %s seconds ---" % (time.time() - start_time))   
    fh.close
    
    """ Horspool algorithm test """
    """
    fh = open('text_sources/test-list.txt', 'r')
    start_time = time.time()
    for line in fh:
        pattern = ''.join(line)
        print("Looking for word - " + pattern)
        f = open('text_sources/wiki-straipsnis-test.txt', 'r')
        occ = preprocess(pattern)
        text=f.read()
        results = horspool_search(text, pattern, occ)
        print(results)
    print("Horspool search took --- %s seconds ---" % (time.time() - start_time))   
    fh.close""" 

    """ KMP algorithm test """
    fh = open('text_sources/test-list.txt', 'r')
    start_time = time.time()
    for line in fh:
        pattern = ''.join(line)
        print("Looking for word - " + pattern)
        f = open('text_sources/wiki-straipsnis.txt', 'r')
        occ = preprocess(pattern)
        text=f.read()
        results = kmp_search(text, pattern)
        print(results)
    print("KMP search took --- %s seconds ---" % (time.time() - start_time))
    fh.close

    """ BruteForce algorithm test """
    fh = open('text_sources/test-list.txt', 'r')
    start_time = time.time()
    for line in fh:
        pattern = ''.join(line)
        print("Looking for word - " + pattern)
        f = open('text_sources/wiki-straipsnis.txt', 'r')
        occ = preprocess(pattern)
        text=f.read()
        results = string_search(text, pattern)
        print(results)
    print("Brute Force search took --- %s seconds ---" % (time.time() - start_time))
    fh.close
