# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        total = 0
        for line in f:
            words = rgx.findall(line)
            for w in words:
                word = w.lower()
                count = 1
                total = total + 1
                # if table doesn't have word, insert word with count = 1
                if not ht.contains_key(word):
                    ht.put(word,count)
                # if table has word, update count and insert word
                else:
                    count = ht.get(word) + 1
                    ht.put(word,count)

    # Build list of tuples from hash table
    tempList = []
    for i in range(ht.capacity):
        while ht._buckets[i].head is not None:
            # get first node using key of head node
            tKey = ht._buckets[i].head.key
            tNode = ht._buckets[i].contains(tKey)
            # insert tNode to wordList as tuple
            tempList.append((tNode.key, tNode.value))
            # remove node from current hash table
            ht.remove(tNode.key)

    # Use word count as key for sort
    def getCount(wordTuple):
        return wordTuple[1]

    # Sort word list
    tempList.sort(key=getCount,reverse=True)

    # Return list with number size
    wordList = []
    for i in range(number):
        wordList.append(tempList[i])

    return wordList

# print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE

# TESTS ONLY FOR PART 3 OF THE ASSIGNMENT

# Test for the empty_buckets() function
def testEmpty(source, size, testFunc):
    ht = HashMap(size,testFunc)

    with open(source) as f:
        total = 0
        for line in f:
            words = rgx.findall(line)
            for w in words:
                word = w.lower()
                count = 1
                total = total + 1
                # if table doesn't have word, insert word with count = 1
                if not ht.contains_key(word):
                    ht.put(word,count)
                # if table has word, update count and insert word
                else:
                    count = ht.get(word) + 1
                    ht.put(word,count)

    return ht.empty_buckets()

# Test for the table_load() function
def testLoad(source, size, testFunc):
    ht = HashMap(size,testFunc)

    with open(source) as f:
        total = 0
        for line in f:
            words = rgx.findall(line)
            for w in words:
                word = w.lower()
                count = 1
                total = total + 1
                # if table doesn't have word, insert word with count = 1
                if not ht.contains_key(word):
                    ht.put(word,count)
                # if table has word, update count and insert word
                else:
                    count = ht.get(word) + 1
                    ht.put(word,count)

    return ht.table_load()

capacity = 1500
source = "alice.txt"

print("Results for empty_buckets():")
print(testEmpty(source,capacity,hash_function_1))
print(testEmpty(source,capacity,hash_function_2))

print("Results for table_load():")
print(testLoad(source,capacity,hash_function_1))
print(testLoad(source,capacity,hash_function_2))