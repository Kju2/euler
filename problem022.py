"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""


def worth_of_name(name):
    """
    >>> worth_of_name("COLIN")
    53
    """
    return sum([ord(c) - ord('A') + 1 for c in name])


def main():
    """
    >>> main()
    871198282
    """
    names = [name[1:-1] for name in open("names.txt").readline().split(',')]
    names = enumerate(sorted(names), start=1)
    scores = (pos * worth_of_name(name) for (pos, name) in names)
    print(sum(scores))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
