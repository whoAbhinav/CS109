# How many unique hands of 5 cards are there in a 52 card deck?
import itertools
import math

VALUES = '23456789TJQKA'
SUITS = 'CDHS'

def main():
    cards = []
    for value in VALUES:
        for suit in SUITS:
            cards.append(value + suit)
    subsets = set(itertools.combinations(cards, 5))
    # for hand in subsets:
    #     print(hand)
    print(len(subsets))

    print(math.factorial(52) / (math.factorial(5) * math.factorial(52-5)))

if __name__ == '__main__':
    main()