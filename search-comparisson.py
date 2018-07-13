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
def boyer_moore_horspool(text, pattern):
    '''
    :param text: (string)
    :param pattern: (string)
    :return: list of indexes where full match occurs
    '''
    t_len = len(text)
    p_len = len(pattern)
    results = []
 
    # Step 1: Preprocess the data
    # Create "bad matches" table (with a size of jump)
    # ord() - As input given "x" char. As output - integer representing the unicode
    T = {i: p_len for i in range(256)}  # table of 256 integers (each char represents as unique integer in unicode)
    for i, char in enumerate(needle):
        T[ord(char)] = p_len - i - 1
 
    # Step 2: Search pattern in the text
    i = 0
 
    while i <= t_len - p_len:
        skip = 0
        text_part = text[i:i + p_len][::-1]
 
        # Iterate over reversed part of text (from right to left)
        for j, current_char in enumerate(text_part):
            # Mismatch found, now we can jump through several indexes
            if pattern[p_len - j - 1] != current_char:
                skip = T[ord(current_char)]
                break
 
        # Finally if we found complete match, we should add its index to results list
        else:
            results.append(i)
            skip = 1
        i += skip
 
    return results




content = "12312541231"
needle = "31"
results = boyer_moore_horspool(content, needle)
 
print(results)