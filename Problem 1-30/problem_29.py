'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''

def encoding(string):
    '''
    >>> encoding('AAAABBBCCDAA')
    '4A3B2C1D2A'
    >>> encoding('')
    ''
    >>> encoding('AaaB')
    '1A2a1B'
    '''
    if not string:
        return ''

    coding = []

    code = string[0]
    for char in string[1:]:
        if char != code[-1]:
            coding.append(str(len(code)) + code[-1])
            code = char
        else:
            code += char

    if code:
        coding.append(str(len(code)) + code[-1])

    return ''.join(coding)

def decoding(code):
    '''
    >>> decoding('4A3B2C1D2A')
    'AAAABBBCCDAA'
    >>> decoding('')
    ''
    >>> decoding('1A2a1B')
    'AaaB'
    '''
    if not code:
        return ''

    decoding = []
    while code:
        to_decode = code[:2]
        string = to_decode[1] * int(to_decode[0])
        decoding.append(string)
        code = code[2:] if len(code) > 2 else []
    return ''.join(decoding)


def others(rle):
    '''
    Refer:
    https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_26_30.py#L97
    >>> others('AAAABBBCCDAA')
    '4A3B2C1D2A'
    >>> others('4A3B2C1D2A')
    'AAAABBBCCDAA'
    '''
    if rle.isalpha():  # no numbers, encode

        encoded = ''
        while rle:

            idx = 0
            while idx < len(rle) and rle[0] == rle[idx]:
                idx += 1

            encoded += str(idx) + rle[0]
            rle = rle[idx:]

        return encoded

    else:  # decode

        return ''.join(c * int(n) for n, c in zip(rle[::2], rle[1::2]))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
