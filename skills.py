# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    
    word_list = string1.split()         # create list of words in string
    d = {}                              # initialize dictionary
    for word in word_list:              # loop through list of words
        if word in d.keys():            # if the word is already in dictionary,
            d[word] += 1                # add 1 to its value
        else:                           # if it isn't there yet,
            d[word] = 1                 # add it with a starting value of 1
                                        # (note: could also have done this with .getdefault, as in next function)
    return d


def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    d1 = {}
    for item in list1:
        d1[item] = d1.setdefault(item, 0) + 1       # create dict of items in list1 and how many times they appear

    d2 = {}
    for item in list2:
        d2[item] = d2.setdefault(item, 0) + 1       # do the same for list2

    common_d = {}
    for key in d1.keys():                           # for each key in d1,
        d1_count = d1[key]                          # assign its value to d1_count
        d2_count = d2.get(key)                      # if the key also appears in d2, assign its value to d2_count (or assign None if it doesn't appear in d2)
        if d2_count != None:                        # if key was found in d2,
            common_d[key] = max(d1_count, d2_count) # add it to common_d with a value of whichever count is greater

    common_list = []                                # initialize list of common items
    for key in common_d.keys():                     # loop through keys in common_d
        common_list += [key] * common_d[key]        # add each one to the list however many times its value indicates
    
    return common_list


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    d1 = { item: 1 for item in list1 }          # create dict of items in list1 (using 1 as placeholder value, not important)
    d2 = { item: 1 for item in list2 }          # do the same for list2     

    common_d = {}
    for key in d1.keys():                       # for each key in d1,
        if d2.get(key) != None:                 # if key is also in d2,
            common_d[key] = 1                   # add key to common_d (again with placeholder value of 1)
 
    common_list = common_d.keys()               # create list of keys in common_d

    return common_list


def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    d = {}
    for item in list1:                                          # for each item in the list,
        if item not in d.keys() and (0-item) not in d.keys():   # if neither it nor its opposite is already a key,
            d[item] = d.setdefault(item, (0 - item))            # create a dict key, with its value being its opposite

    pair_list = [ [key, d[key]] for key in d if d[key] in list1 ] # create a list containing lists of each key and its opposite

    return pair_list


def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    d = { word: 1 for word in words}        # create a dictionary with each word as a key (and 1 as a placeholder value)

    no_dups_list = [ key for key in d.keys() ]  # build a list of keys in d

    return no_dups_list


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

        >>> word_length(["this", "is", "an", "extra", "doctest"])
        [(2, ['is', 'an']), (4, ['this']), (5, ['extra']), (7, ['doctest'])]

    """

    d = {}

    for word in words:                                  # for each word,
        d.setdefault(len(word), []).append(word)        # create a key for the length (or find existing key) and add word to its value list

    sorted_keys = sorted(d)                             # make a list of the keys in ascending order
    list_of_tuples = [ (key, d[key]) for key in sorted_keys ]   # build a list containing tuples of each word length and its list of words

    return list_of_tuples


def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_vocab = { 'sir': 'matey',                # store each word and its translation to a dictionary
                    'hotel': 'fleabag inn',
                    'student': 'swabbie',
                    'boy': 'matey',
                    'madam': 'proud beauty',
                    'professor': 'foul blaggart',
                    'restaurant':  'galley',
                    'your': 'yer',
                    'excuse': 'arr',
                    'students': 'swabbies',
                    'are': 'be',
                    'lawyer': 'foul blaggart',
                    'the': "th'",
                    'restroom': 'head',
                    'my': 'me',
                    'hello': 'avast',
                    'is': 'be',
                    'man': 'matey' }
    
    phrase_list = phrase.split()                # split phrase into a list of words

    for i in range(len(phrase_list)):           # loop through list by index
        word = phrase_list[i]
        phrase_list[i] = pirate_vocab.get(word, word)   # replace each word with its translation if it's in pirate_vocab, or with itself if it's not

    translated = " ".join(phrase_list)          # join the list back into a string

    return translated


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    d = {}

    for word in words:                              # for each word,
        d.setdefault(len(word), []).append(word)    # create a key for its length, or find existing key, and add word to its value list

    for key in d.keys():
        d[key].sort()                               # sort each value list alphabetically

    sorted_keys = sorted(d)                         # make a list of the keys in ascending order
    list_of_tuples = [ (key, d[key]) for key in sorted_keys ]   # build a list containing tuples of each word length and its list of words

    return list_of_tuples


##############################################################################
# You can ignore everything after here

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
