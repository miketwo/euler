#!/usr/bin/env python
'''
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD    Player 2
        Pair of Fives       Pair of Eights

2       5D 8C 9S JS AC      2C 5C 7D 8S QH    Player 1
        Highest card Ace    Highest card Queen

3       2D 9C AS AH AC      3D 6D 7D TD QD    Player 2
        Three Aces           Flush with Diamonds

4       4D 6S 9H QH QC      3D 6D 7H QD QS    Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D    Player 1
        Full House          Full House
        With Three Fours     with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
import unittest
from functools import total_ordering
from itertools import groupby

HAND_VALUES = {
    "High Card": 0,
    "One Pair": 1,
    "Two Pairs": 2,
    "Three of a Kind": 3,
    "Straight": 4,
    "Flush": 5,
    "Full House": 6,
    "Four of a Kind": 7,
    "Straight Flush": 8,
    "Royal Flush": 9,
}


@total_ordering
class Card(object):
    def __init__(self, text):
        self.text = text
        value = text[0]
        suit = text[1]
        valmap = {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        if value in valmap:
            value = valmap[value]
        value = int(value)
        assert suit in list('SCHD'), "Bad Suit is {}".format(suit)
        assert value >= 2 and value <= 14, "Bad Range is {}".format(value)
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __lt__(self, other):
        return self.value < other.value


@total_ordering
class Hand(object):
    def __init__(self, text):
        self.cards = [Card(x) for x in text.split()]
        self.values = [c.value for c in sorted(self.cards)]
        self.suits = [c.suit for c in sorted(self.cards)]
        self.value = self.compute_value()

    def __str__(self):
        return str(self.cards)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __lt__(self, other):
        return self.value < other.value

    def compute_value(self):
        return 0

    def group(self):
        print [list(group) for key, group in groupby(self.values)]
        return [len(list(group)) for key, group in groupby(self.values)]

    def _4k(self):
        pass
        # if 4 in self.group():
            # return (HAND_VALUES['Four of a Kind'], #value of 4k, #value of other card)

    def _3k(self):
        return 3 in self.group()

    def _2k(self):
        return 2 in self.group()

    def _isRF(self):
        return self._isSF() and self._highcard() == 14

    def _isSF(self):
        return self._isStraight() and self._isFlush()

    def _isFlush(self):
        return len(set(self.suits)) == 1

    def _isStraight(self):
        return [x-self.values[0] for x in self.values] == [0, 1, 2, 3, 4]

    def _highcard(self):
        return self.values[-1]

    def _lowcard(self):
        return self.values[0]


def hands_from_line(line):
    # Given a line, returns two hands
    a = " ".join(line.split()[:5])
    b = " ".join(line.split()[5:])
    return Hand(a), Hand(b)


def main():
    tests()


class BasicTests(unittest.TestCase):

    def test_blah(self):
        print Hand('5H 5C 6S 7S KD').group()
        print Hand('5D 8C 9S JS AC').group()
        print Hand('2D 9C AS AH AC').group()
        print Hand('4D 6S 9H QH QC').group()
        print Hand('2H 2D 4C 4D 4S').group()
        print Hand('2H 2D 4C 4D 5S').group()

    def test_init(self):
        # None of these should throw
        Card('2H')
        Card('AD')
        Card('JC')
        Card('TH')
        Hand('5H 5C 6S 7S KD')
        Hand('5D 8C 9S JS AC')
        Hand('2D 9C AS AH AC')
        Hand('4D 6S 9H QH QC')
        Hand('2H 2D 4C 4D 4S')

    def test_hands_from_line(self):
        line = '5H 5C 6S 7S KD 2C 3S 8S 8D TD'
        expected = Hand('5H 5C 6S 7S KD'), Hand('2C 3S 8S 8D TD')
        result = hands_from_line(line)
        self.assertEqual(expected, result)

    def test_equality_cards(self):
        self.assertTrue(Card('5H') == Card('5H'))

    def test_equality_hands(self):
        self.assertTrue(Hand('5H 5C 6S 7S KD') == Hand('5H 5C 6S 7S KD'))

    def test_card_sorting(self):
        cards = [Card(x) for x in '5H 5C 6S 7S KD'.split()]
        expected = '[KD, 7S, 6S, 5H, 5C]'
        result = str(sorted(cards, reverse=True))
        self.assertEqual(expected, result)

    def test_highcard(self):
        h = Hand('JD TD AD QD KD')
        self.assertEqual(h._highcard(), 14)

    def test_RF(self):
        h = Hand('JD TD KD QD AD')
        result = h._isRF()
        self.assertTrue(result)

        h = Hand('JD TD KD QD AC')
        result = h._isRF()
        self.assertFalse(result)

        h = Hand('JD TD 9D QD AC')
        result = h._isRF()
        self.assertFalse(result)

    def test_SF(self):
        h = Hand('9D 6D 5D 8D 7D')
        result = h._isSF()
        self.assertTrue(result)

        h = Hand('9D 6D 5D 8C 7D')
        result = h._isSF()
        self.assertFalse(result)

        h = Hand('9D 6D 5D TD 7D')
        result = h._isSF()
        self.assertFalse(result)



class ComparisonTests(unittest.TestCase):
    def test_one_pair(self):
        # One pair
        h1, h2 = Hand('5H 5C 6S 7S KD'), Hand('2C 3S 8S 8D TD')
        self.assertTrue(h2 > h1)

        # One pair
        h1, h2 = Hand('9H 9C 6S 7S KD'), Hand('2C 3S 8S 8D TD')
        self.assertTrue(h1 > h2)

    def test_highest_card(self):
        # Highest card
        h1, h2 = Hand('5D 8C 9S JS AC'), Hand('2C 5C 7D 8S QH')
        self.assertTrue(h1 > h2)

        # Highest card
        h1, h2 = Hand('5D 8C 9S JS TC'), Hand('2C 5C 7D 8S QH')
        self.assertTrue(h2 > h1)

    def test_three_vs_flush(self):
        # 3 Aces vs Flush (flush should win)
        h1, h2 = Hand('2D 9C AS AH AC'), Hand('3D 6D 7D TD QD')
        self.assertTrue(h2 > h1)
        self.assertFalse(h1 > h2)

    def test_matching_pair_high_card(self):
        h1, h2 = Hand('4D 6S 9H QH QC'), Hand('3D 6D 7H QD QS')
        self.assertTrue(h1 > h2)
        self.assertFalse(h2 > h1)

    def test_full_house(self):
        h1, h2 = Hand('2H 2D 4C 4D 4S'), Hand('3C 3D 3S 9S 9D')
        self.assertTrue(h1 > h2)
        self.assertFalse(h2 > h1)


if __name__ == '__main__':
    unittest.main()
