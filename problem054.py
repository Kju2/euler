"""
http://projecteuler.net/problem=54
"""

import collections

# ranks
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

# card values
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10
JACK = 11
QUEEN = 12
KING = 13
ACE = 14
VALUES = {'2': TWO, '3': THREE, '4': FOUR, '5': FIVE, '6': SIX,
          '7': SEVEN, '8': EIGHT, '9': NINE, 'T': TEN, 'J': JACK,
          'Q': QUEEN, 'K': KING, 'A': ACE}


class Hand(object):
    """
    A Hand represents the five cards of one poker player.
    """
    def __init__(self, encoded_cards):
        self.values = [VALUES[card[0]] for card in encoded_cards]
        self.values.sort()
        self.values.reverse()

        self.flush = len(set([card[1] for card in encoded_cards])) == 1

        assert len(self.values) == 5
        assert isinstance(self.flush, bool)

    @property
    def rank(self):
        """
        Computes the rank of the hand.
        """

        values = self.values
        straigt_values = list(range(values[0], values[0]-5, -1))

        if self.flush:
            if values[-1] == TEN:
                return ROYAL_FLUSH, values
            if values == straigt_values:
                return STRAIGHT_FLUSH, values

        counter = collections.Counter(values)
        most_common = counter.most_common()
        if most_common[0][1] == 4:
            return FOUR_OF_A_KIND, most_common[0][0], values

        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return FULL_HOUSE, most_common[0][0], most_common[1][0], values

        if self.flush:
            return FLUSH, values

        if values == straigt_values:
            return STRAIGHT, values

        if most_common[0][1] == 3:
            return THREE_OF_A_KIND, most_common[0][0], values

        if most_common[0][1] == 2 and most_common[1][1] == 2:
            reverse_sorted_pairs = [most_common[0][0], most_common[1][0]]
            reverse_sorted_pairs.sort()
            reverse_sorted_pairs.reverse()
            return TWO_PAIRS, reverse_sorted_pairs, values

        if most_common[0][1] == 2:
            return ONE_PAIR, most_common[0][0], values

        return HIGH_CARD, values

    def wins_against(self, opponent):
        """
        Computes who wins the poker game.
        """

        for (s, o) in zip(self.rank, opponent.rank):
            if s > o:
                return True
            elif s < o:
                return False
            else:
                continue
        return False


def main():
    """
    >>> main()
    376
    """
    assert Hand(['TH', 'JH', 'QH', 'KH', 'AH']).rank[0] == ROYAL_FLUSH
    assert Hand(['2H', '3H', '4H', '5H', '6H']).rank[0] == STRAIGHT_FLUSH
    assert Hand(['2H', '2C', '2S', '2D', 'AH']).rank[0] == FOUR_OF_A_KIND
    assert Hand(['2H', '2C', '2D', '9H', '9D']).rank[0] == FULL_HOUSE
    assert Hand(['2H', '4H', '8H', '9H', 'AH']).rank[0] == FLUSH
    assert Hand(['2H', '3C', '4D', '5H', '6H']).rank[0] == STRAIGHT
    assert Hand(['2H', '2C', '2D', '5H', '6H']).rank[0] == THREE_OF_A_KIND
    assert Hand(['2H', '2C', '5D', '5H', '6H']).rank[0] == TWO_PAIRS
    assert Hand(['2H', '2C', '4D', '5H', '6H']).rank[0] == ONE_PAIR
    assert Hand(['2H', '3C', '4D', '5H', '9H']).rank[0] == HIGH_CARD
    assert Hand(['5H', '5C', '6S', '7S', 'KD']).rank[0] == ONE_PAIR
    assert Hand(['2C', '3S', '8S', '8D', 'TD']).rank[0] == ONE_PAIR
    assert Hand(['5D', '8C', '9S', 'JS', 'AC']).rank[0] == HIGH_CARD
    assert Hand(['2C', '5C', '7D', '8S', 'QH']).rank[0] == HIGH_CARD
    assert Hand(['2D', '9C', 'AS', 'AH', 'AC']).rank[0] == THREE_OF_A_KIND
    assert Hand(['3D', '6D', '7D', 'TD', 'QD']).rank[0] == FLUSH
    assert Hand(['4D', '6S', '9H', 'QH', 'QC']).rank[0] == ONE_PAIR
    assert Hand(['3D', '6D', '7H', 'QD', 'QS']).rank[0] == ONE_PAIR
    assert Hand(['2H', '2D', '4C', '4D', '4S']).rank[0] == FULL_HOUSE
    assert Hand(['3C', '3D', '3S', '9S', '9D']).rank[0] == FULL_HOUSE

    with open("problem054.txt") as f:
        games = f.read().splitlines()

    games = [game.split(' ') for game in games]
    games = [(Hand(game[:5]), Hand(game[5:])) for game in games]

    print(sum((p1.wins_against(p2) for (p1, p2) in games)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
