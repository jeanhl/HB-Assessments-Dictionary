"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
import random

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    words = {}
    
    # turns input into a list of strings
    phrase = phrase.split()
    print phrase

    # makes a dictinary of letters and the number of appearance
    for word in phrase:
        words[word] = words.get(word, 0) + 1

    return words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """

    # Assuming the melons and their prices are given in dictionary format

    price_of_melon = melon_dictionary[melon_name]

    return price_of_melon


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    words_dict = {}

    words = set(words)
    words = list(words)

    for i in range(len(words)):
        word = words[i]
        count = len(word)
        if count in words_dict:
            current_words = [words_dict[count]]
            current_words.append(word)
            words_dict[count] = current_words
        else:
            words_dict[count] = word

    # print words_dict

    answer_lst = []
    for thing in words_dict:
        tups_val = words_dict[thing]
        if tups_val is not list:
            tups_val = [tups_val]
        else:
            pass
        tups = (thing, tups_val)
        answer_lst.append(tups)

    # current it returns a list in a list if the value is already a list. 
    # COME BACK AND FIX IT !!!!
    return answer_lst


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Turn the list of words into a dictionary called "pirate_dict"
    # Need to add in the pirate_dict here. 
    # Having issues with .split() and .strip()

    pirate_dict = {}

    for word in phrase:
        if word in pirate_dict:
            pirate_word = pirate_dict[word]
            word = pirate_word
        else:
            pass

    return phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    
    last_dict = {}
    first_dict = {}

    # make a dictionary where keys are the last letters and the values are the
    # words 
    for word in names:
        last_dict[word] = word[-1] # {word:last letter}
        first_dict[word[0]] = word # {first letter:word}



    length = len(names)
    choice = random.randint(0, (length - 1))
    output = [names[choice]] 
    # now we have a list of 1 random word from names

    flag = output[-1] # gives the last word in the list
   
    while flag in last_dict:
        next_letter = flag[-1]
        possibles = [first_dict[next_letter]]
        choosen = random.choice(possibles)
        if choosen[-1] in first_dict:
            output.append(choosen)
            flag = output[-1]
        else:
            return output


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
