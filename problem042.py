"""
The n^th term of the sequence of triangle numbers is given by,
t_n = 0.5 * n * (n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for 'SKY' is 19 + 11 + 25 = 55 = t_10. If the word
value is a triangle number then we shall call the word a triangle word.

Using the list of words, containing nearly two-thousand common English words,
how many are triangle words?
"""


def char_in_alphabet(char):
    """
    char_in_alphabet returns the alphabetical value of an uppercase letter.
    """
    return ord(char) - ord('A') + 1


def is_triangle_word(word):
    """
    is_triangle_word tests if the sum of character values is a triangle number.
    """
    word_value = sum([char_in_alphabet(c) for c in word])

    triangle_numbers = {}
    index = 1
    number = 1
    while number <= word_value:
        triangle_numbers[number] = index
        index += 1
        number += index
    return word_value in triangle_numbers


def main():
    """
    >>> main()
    162
    """
    with open("problem042.txt") as f:
        words = f.read().splitlines()

    print(len([w for w in words if is_triangle_word(w)]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
