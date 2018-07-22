'''
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer
line length k, return a list of strings which represents each line, fully
justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed
as equally as possible, with the extra spaces, if any, distributed starting
from the left.

If you can only fit one word on a line, then you should pad the right-hand side
with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and
k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def justify_words(words, k):
    '''
    Justify a list of words
    Args:
        words(list)
        k(int)
    Returns:
        list
    '''
    res = []

    len_words = num_word = 0
    line_words = []

    for word in words:
        if len(word) + len_words + num_word > k:
            line = justify_line(line_words, k, len_words, num_word)
            res.append(line)

            # re-initialize
            len_words = num_word = 0
            line_words = []

        line_words.append(word)
        len_words += len(word)
        num_word += 1

    if line_words:
        line = justify_line(line_words, k, len_words, num_word)
        res.append(line)
    return res


def justify_line(line_words, k, len_words, num_word):
    '''
    Args:
        line_words(list)
        k(int)
        len_words(int)
        num_word(int)
    Returns:
        string
    '''
    if num_word == 1:
        return line_words[0] + ' ' * (k - len(line_words[0]))

    num_space_total = k - len_words
    remainder = num_space_total % (num_word - 1)
    num_space = num_space_total / (num_word - 1)

    if remainder == 0:  # spaces are equally distributed
        space = ' ' * num_space
        return space.join(line_words)
    else:   # front half has more space than latter half
        space = ' ' * num_space
        line_words[remainder] = space.join(line_words[remainder:])
        front_space = ' ' * (num_space + 1)
        return front_space.join(line_words[:remainder + 1])


def main():
    '''
    >>> words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    >>> k = 16
    >>> justify_words(words, k)
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']

    >>> words = ['the']
    >>> k = 5
    >>> justify_words(words, k)
    ['the  ']

    >>> words = ["the", "quick", "brown", "fox"]
    >>> k = 16
    >>> justify_words(words, k)
    ['the  quick brown', 'fox             ']
    '''

    import doctest
    doctest.testmod(verbose = True)


if __name__ == '__main__':
    main()
